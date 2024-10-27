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

"""This module contains a simple class for managing MS/MS spectrum."""


class MSMSSpectrum:
    """A class for managing MS/MS spectrum."""

    def __init__(self, title=None):
        """Initialize the MSMSSpectrum class."""
        self.title = title
        self.rtinseconds = None
        self.pepmass = None
        self.charge = None
        self.peaks = []

    def set_title(self, title):
        """Set the title."""
        self.title = title

    def set_rtinseconds(self, rtinseconds):
        """Set rtinseconds."""
        self.rtinseconds = float(rtinseconds)

    def set_pepmass(self, pepmass):
        """Set pepmass."""
        self.pepmass = float(pepmass)

    def set_charge(self, charge):
        """Set the charge."""
        self.charge = charge

    def append_peak(self, peak):
        """Append spectrum data."""
        self.peaks.append(peak)

    def get_exact_mass(self):
        """Return the exact mass."""
        return self.pepmass

    def get_rtinseconds(self):
        """Return the time of the spectrum."""
        return self.rtinseconds

    def get_peaks(self):
        """Return the list of fragments."""
        return self.peaks
