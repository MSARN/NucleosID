# Copyright 2022 CNRS and University of Strasbourg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module provides a class for analysing data of a MGF data file."""

import pandas as pd


class MGFDataAnalyzer(object):
    """A class for analysing MGF data and finding RNA modifications."""

    def __init__(self, ms_ms_spectra, arn_modifications, analysis_parameters):
        """Initialize the MGFDataAnalyszer class."""
        self.exclusion_time = analysis_parameters['exclusion_time']
        self.ms_tolerance = analysis_parameters['ms_tolerance']
        self.ms_tolerance_type = analysis_parameters['ms_tolerance_type']
        self.ms_ms_tolerance_type = analysis_parameters['ms_ms_tolerance_type']
        self.ms_ms_tolerance = analysis_parameters['ms_ms_tolerance']
        self.ms_ms_score_threshold = analysis_parameters['ms_ms_score_threshold']
        self.exclusion_time = analysis_parameters['exclusion_time']
        """Initialize the SpectrumAnalyzer class."""
        self.ms_ms_spectra = ms_ms_spectra
        self.arn_modifications = arn_modifications
        self.arn_analysis = pd.DataFrame({
            'Modification': pd.Series(dtype='str'),
            'Observed MS (Da)': pd.Series(dtype='float'),
            'Theoretical MS (Da)': pd.Series(dtype='float'),
            'Observed MS/MS (Da)': pd.Series(dtype='float'),
            'Theoretical MS/MS (Da)': pd.Series(dtype='float'),
            'Score (%)': pd.Series(dtype='float'),
            'Detection time (s)': pd.Series(dtype='float')
        })
        self.filtered_number = 0

    def find_arn_modifications(self):
        """Analyse ARN modifications in the spectrum."""
        matching_modifications = {}
        raw_hit_number = 0
        for spectrum in self.ms_ms_spectra:
            exact_mass = spectrum.get_exact_mass()
            for mod_name in self.arn_modifications:
                modified_mass = self.arn_modifications[mod_name]['ms_value']
                if self.ms_tolerance_type == 'ppm':
                    delta = abs(exact_mass - modified_mass)/modified_mass * 1000000
                else:
                    delta = abs(exact_mass - modified_mass)
                if delta <= self.ms_tolerance:
                    # A matching mass has been found
                    peaks = spectrum.get_peaks()
                    matching_peaks = {}
                    modified_frag_masses = self.arn_modifications[mod_name]['ms_ms_values']
                    max_intensity = 0
                    # Max intensity for the current modification matching a fragment
                    # spectrum
                    mfrag_intensity = 0
                    for (frag_mass, intensity) in peaks:
                        max_intensity = max(max_intensity, intensity)
                        for modified_frag_mass in modified_frag_masses:
                            if self.ms_ms_tolerance_type == 'ppm':
                                diff = abs(frag_mass - modified_frag_mass) / modified_frag_mass * 1000000
                            else:
                                diff = abs(frag_mass - modified_frag_mass)
                            if diff <= self.ms_ms_tolerance:
                                mfrag_intensity = max(intensity, mfrag_intensity)
                                if modified_frag_mass not in matching_peaks:
                                    # We need to register intensity as we only
                                    # store the frag_mass with the higher
                                    # intensity corresponding to a
                                    # modified_frag_mass
                                    matching_peaks[modified_frag_mass] = (
                                        frag_mass, intensity
                                    )
                                else:
                                    # A peak for this fragment has already
                                    # been found
                                    if intensity > matching_peaks[modified_frag_mass][1]:
                                        matching_peaks[modified_frag_mass] = (
                                            frag_mass, intensity
                                        )
                    if matching_peaks:
                        raw_hit_number += 1
                        frag_max_intensity = 0
                        frag_masses = []
                        # Compute the score for each result
                        for key_mass in matching_peaks:
                            frag_max_intensity = max(
                                matching_peaks[key_mass][1],
                                frag_max_intensity
                            )
                            frag_masses.append(matching_peaks[key_mass][0])

                        if max_intensity == 0:
                            score = 0
                        else:
                            score = frag_max_intensity / max_intensity
                        if (score * 100) > self.ms_ms_score_threshold:
                            matching_masses = ';'.join([str(x) for x in frag_masses])
                            mod_frag_masses = ';'.join([str(y) for y in modified_frag_masses])
                            if mod_name not in matching_modifications:
                                matching_modifications[mod_name] = []

                            matching_modifications[mod_name].append({
                                'exact_mass': exact_mass,
                                'modified_mass': modified_mass,
                                'matching_masses': matching_masses,
                                'mod_frag_masses': mod_frag_masses,
                                'score': round(score*100, 2),
                                'intensity': frag_max_intensity,
                                'rtinseconds': spectrum.get_rtinseconds()
                            })
        # Filter results based on the detection time
        filtered_modifications = self.filter_result_by_detection_time(
            matching_modifications
        )

        filtered_hit_number = 0

        # Only modification where ms ms match is added!
        for modification_type in filtered_modifications:
            for modification in filtered_modifications[modification_type]:
                # Add the missing analysis value
                filtered_hit_number += 1
                self.arn_analysis.loc[len(self.arn_analysis.index)] = [
                    modification_type,
                    modification['exact_mass'],
                    modification['modified_mass'],
                    modification['matching_masses'],
                    modification['mod_frag_masses'],
                    modification['score'],
                    modification['rtinseconds'],
                ]
        self.filtered_number = raw_hit_number - filtered_hit_number

    def filter_result_by_detection_time(self, modifications):
        """Filter modifications by detection time."""
        filtered_modifications = {}
        for mod_name in modifications:
            for modification in modifications[mod_name]:
                if mod_name not in filtered_modifications:
                    filtered_modifications[mod_name] = [
                        modification
                    ]
                else:
                    cursor = len(filtered_modifications[mod_name]) - 1
                    previous_time = filtered_modifications[mod_name][cursor]['rtinseconds']
                    current_time = modification['rtinseconds']
                    if abs(current_time - previous_time) < self.exclusion_time:
                        # Select the peak with the highst intensity
                        if modification['intensity'] > \
                                filtered_modifications[mod_name][cursor]['intensity']:
                            filtered_modifications[mod_name][cursor] = modification
                    else:
                        filtered_modifications[mod_name].append(
                            modification
                        )
        return filtered_modifications

    def get_analysis(self):
        """Return the result of ARN modification analysis."""
        return self.arn_analysis
