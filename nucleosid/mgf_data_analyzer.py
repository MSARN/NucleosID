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

"""This module provides a class for analysing data of a MGF data file ."""

import pandas as pd


class MGFDataAnalyzer(object):
    """A class for analysing MGF data and finding RNA modifications."""

    def __init__(self, ms_ms_spectra, arn_modifications, analysis_parameters):
        """Initialize the MGFDataAnalyszer class."""
        self.exclusion_time = analysis_parameters['exclusion_time']
        self.ms_tolerance = analysis_parameters['ms_tolerance']
        self.ms_ms_tolerance = analysis_parameters['ms_ms_tolerance']
        """Initialize the SpectrumAnalyzer class."""
        self.ms_ms_spectra = ms_ms_spectra
        self.arn_modifications = arn_modifications
        self.arn_analysis = pd.DataFrame({
            'Modification': pd.Series(dtype='str'),
            'Observed MS (Da)': pd.Series(dtype='float'),
            'Theoretical MS (Da)': pd.Series(dtype='float'),
            'Observed MS/MS (Da)': pd.Series(dtype='float'),
            'Theoretical MS/MS (Da)': pd.Series(dtype='float'),
            'Relative intensity (%)': pd.Series(dtype='float'),
            'Start analysis (s)': pd.Series(dtype='float')
        })

    def find_arn_modifications(self):
        """Analyse ARN modifications in the spectrum."""
        for spectrum in self.ms_ms_spectra:
            exact_mass = spectrum.get_exact_mass()
            # Don't check time now
            # time = spectrum.get_time()
            # Si la masse est celle de la modif, alors
            for modification_name in self.arn_modifications:
                hit_found = False
                modified_mass = self.arn_modifications[modification_name]['ms_value']
                delta = abs(
                    exact_mass - modified_mass
                )
                if delta <= self.ms_tolerance:
                    peaks = spectrum.get_peaks()
                    matching_peaks = []
                    modified_frag_masses = self.arn_modifications[modification_name]['ms_ms_values']
                    for modified_frag_mass in modified_frag_masses:
                        for (frag_mass, intensity) in peaks:
                            diff = abs(frag_mass - float(modified_frag_mass))
                            if diff <= self.ms_ms_tolerance:
                                matching_peaks.append(round(frag_mass))
                                hit_found = True
                    if hit_found:
                        # Add the missing analysis value
                        self.arn_analysis.loc[len(self.arn_analysis.index)] = [
                            modification_name,
                            exact_mass,
                            modified_mass,
                            ';'.join([str(x) for x in matching_peaks]),
                            ';'.join([str(y) for y in modified_frag_masses]),
                            0,
                            0
                        ]

    def get_analysis(self):
        """Return the result of ARN modification analysis."""
        return self.arn_analysis
