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

"""This module provides a class for writing result output of analysis."""

import pandas as pd


class AnalysisWriter(object):
    """A class for writing analysing results."""

    def __init__(self, data):
        """Initialize the AnalysisWriter class."""
        self.data = data

    def write_analysis(self, filename, filetype="csv"):
        """Analyse ARN modifications in the spectrum."""
        if filetype == 'xlsx':
            self.write.xlsx_output(filename)
        else:
            self.write_csv_output(filename)

    def write_csv_output(self, filename):
        """Write results as a CSV file."""
        self.data.to_csv(
            filename, index=False,
            sheet_name="Nucleosid_Results"
        )

    def write_xlsx_output(self, filename):
        """Write results as an excel file."""
        with pd.ExcelWriter(filename) as writer:
            self.data.to_excel(writer, index=False)
