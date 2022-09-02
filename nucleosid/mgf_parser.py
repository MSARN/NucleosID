# Copyright 2022 CNRS and University of Strasbourg
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


class MgfParser(object):
    """A class for parsing a MFG file."""

    def __init__(self, filename):
        """Initialize the MgfParser class.

        :param str filename: a file with data in MGF format.
        """
        with open(filename, 'r') as mgf_file:
            contents = mgf_file.readlines()
            self._parsemg_data(contents)
        self.spectra = []

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
                spectrum = {'data': []}
            elif stripped_line == 'END IONS':
                # End of the spectrum
                self.spectra.append(spectrum)
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
                        spectrum[key] = value
            else:
                if in_ions:
                    # mass spectrum data
                    spectrum_data = splitted_line.strip()
                    spectrum['data'].append((
                        float(spectrum_data[0]), float(spectrum_data[1])
                    ))

    def get_spectra(self):
        """Return the spectra."""
        return self.spectra
