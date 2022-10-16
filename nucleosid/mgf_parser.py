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

"""This module permits to parse a MGF file."""

import numpy as np

from nucleosid import ms_ms_spectrum


class MgfParser(object):
    """A class for parsing a MFG file."""

    def __init__(self, filename):
        """Initialize the MgfParser class.

        :param str filename: a file with data in MGF format.
        """
        self.ms_ms_spectra = []
        with open(filename, 'r') as mgf_file:
            contents = mgf_file.readlines()
            self._parse_mgf_data(contents)

    def _parse_mgf_data(self, mgf_data):
        """Read the header and store the information.

        :param list header_line: a list of line
        """
        in_header = True
        in_ions = False
        header = {}
        for line in mgf_data:
            stripped_line = line.strip()
            if stripped_line == 'BEGIN IONS':
                in_header = False
                in_ions = True
                # A new spectrum
                spectrum = ms_ms_spectrum.MSMSSpectrum()
            elif stripped_line == 'END IONS':
                # End of the spectrum
                self.ms_ms_spectra.append(spectrum)
                in_ions = False
            elif '=' in stripped_line:
                # a key / value parameter
                splitted_line = stripped_line.split('=')
                if len(splitted_line) == 2:
                    key = splitted_line[0].strip().upper()
                    value = splitted_line[1].strip()
                    if in_header:
                        header[key] = value
                    else:
                        if key == 'TITLE':
                            spectrum.set_title(value)
                        elif key == 'RTINSECONDS':
                            spectrum.set_rtinseconds(value)
                        elif key == 'PEPMASS':
                            clean_value = value.split()[0]
                            spectrum.set_pepmass(clean_value)
                        elif key == 'CHARGE':
                            spectrum.set_charge(value)
            else:
                if in_ions:
                    # Mass spectrum peak
                    data = stripped_line.split()
                    if len(data) < 2:
                        # This should raise an error, as we only should have,
                        # at least, a mass value followed by and intensity
                        pass
                    else:
                        spectrum.append_peak((
                            float(data[0]), float(data[1])
                        ))

    def get_ms_ms_spectra(self):
        """Return the spectra."""
        return self.ms_ms_spectra

    def get_peak_list(self):
        """Return the list of peaks."""
        data = np.array()
        for spectrum in self.ms_ms_spectra:
            data = data.append(spectrum['data'])
        return data
