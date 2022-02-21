"""
.. moduleauthor:: Eric Torres

Tests for the rbackup.config module.
"""
import unittest

import file_scripts.editor as editor

# ========== Constants ==========
# ========== Tests ==========

"""Test the select_editor() function.

    Test cases
    -----------
    * Returned object is an instance of str
    * If override is not None, ensure that it is in the result

"""


class TestSelectEditor(unittest.TestCase):
    def test_override(self):
        override = "doesnotexist"
        with self.assertRaises(FileNotFoundError):
            editor.select_editor(override)
