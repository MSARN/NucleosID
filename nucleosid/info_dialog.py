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

"""This module provides a class for displaying information."""

import tkinter as tk
from tkinter import simpledialog


class InfoDialog(simpledialog.Dialog):
    """A simple class for displaying information."""

    def __init__(self, parent, title, text):
        """Initialize the InfoDialog class."""
        self.text = text
        super().__init__(parent, title)

    def body(self, master):
        """Create the main content."""
        # Try to guess the best window width
        max_size = 0
        splitted_text = self.text.split("\n")
        for line in splitted_text:
            max_size = max(len(line), max_size)

        # Create the main text label
        self.message_label = tk.Label(
            master,
            width=max_size,
            text=self.text
        )
        self.message_label.pack()

        return master

    def buttonbox(self):
        """Define a simple OK button."""
        box = tk.Frame(self)
        default_button = tk.Button(
            box, text='OK', width=10, command=self.ok
        )
        default_button.pack()
        self.bind("<Return>", self.ok)
        box.pack()
