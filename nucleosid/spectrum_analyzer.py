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

"""This module provides a class for analysing data of a MS spectrum."""


class SpectrumAnalyzer(object):
    """A class for analysing spectrum data and finding RNA modifications."""

    def __init__(self, spectrum_data, arn_modifications):
        """Initialize the SpectrumAnalyzer class."""
        self.spectrum_data = spectrum_data
        self.arn_modifications = arn_modifications
        self.arn_modification_analysis = {}

    def analyze_arn_modifications(self):
        """Analyse ARN modifications in the spectrum."""
        pass

    def get_analysis(self):
        """Return the result of ARN modification analysis."""
        return self.arn_modification_analysis
