# Copyright 2024 CNRS and University of Strasbourg
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

"""Analysis writer test class."""

import os
import pandas as pd
import pytest

from nucleosid import analysis_writer


@pytest.fixture(scope="session")
def test_write_analysis(tmpdir_factory):
    """Test the write_analysis function."""
    data = pd.DataFrame({
        'Modification': pd.Series(dtype='str'),
        'Observed MS (Da)': pd.Series(dtype='float'),
        'Theoretical MS (Da)': pd.Series(dtype='float'),
        'Observed MS/MS (Da)': pd.Series(dtype='float'),
        'Theoretical MS/MS (Da)': pd.Series(dtype='float'),
        'Score (%)': pd.Series(dtype='float'),
        'Detection time (s)': pd.Series(dtype='float')
    })

    writer = analysis_writer.AnalysisWriter(data)
    output_file = tmpdir_factory.mktemp("data").join("test.csv")
    writer.write_analysis(output_file)
    assert os.path.isfile(output_file)
    output_file = tmpdir_factory.mktemp("data").join("test.xlsx")
    writer.write_analysis(output_file)
    assert os.path.isfile(output_file)
