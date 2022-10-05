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

"""This module permits to parse ARN modification databases."""

import numpy as np
import pandas as pd


class ModificationDatabaseParser(object):
    """A class for parsing an ARN modification database file."""

    COLUMN_TYPES = {
        'Short Name': np.dtype('O'),
        '[M+H]+': np.dtype('float64'),
        'Product ions': np.dtype('O')
    }

    def __init__(self, database_file):
        """Initialize the DatabaseParser class."""
        self.modification_database = {}
        with open(database_file) as database:
            database_df = pd.read_csv(database)
            if self.verify_database_structure(database_df):
                self._parse_database(database_df)

    def verify_database_structure(self, data):
        """Check the consistency of the database."""
        if len(data.dtypes) != len(self.COLUMN_TYPES):
            return False
        for column in data.columns:
            if str(column) not in self.COLUMN_TYPES.keys():
                return False
            if data.dtypes[column] != self.COLUMN_TYPES[column]:
                return False
        return True

    def _parse_database(self, database):
        """Parse a Nucleos'ID database file."""
        for item in database.itertuples():
            name = item[1]
            ms_value = item[2]
            ms_ms_value = item[3].split(';')
            self.modification_database[name] = {
                'ms_value': float(ms_value),
                'ms_ms_values': ms_ms_value
            }

    def get_modification_database(self):
        """Return the database as a panda object."""
        return self.modification_database
