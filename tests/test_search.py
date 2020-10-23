"""
.. moduleauthor:: Eric Torres

Tests for the rbackup.config module.
"""
import subprocess
import unittest
from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import text, lists

import file_scripts.search as search

# ========== Constants ==========
TESTING_PACKAGE = "file_scripts"
TESTING_MODULE = f"{TESTING_PACKAGE}.search"

# ========== Tests ==========
"""Test the find_files() function.

    Test cases
    -----------
    * Both cases of capture_text
    * bin_override behaves correctly
    * directory is not None
"""


class TestFindFiles(unittest.TestCase):
    def setUp(self):
        self.patched_subprocess = patch(f"{TESTING_MODULE}.subprocess.run")

        self.mocked_run = self.patched_subprocess.start()

    @given(test_override=text(), test_opts=lists(text()))
    def test_bin_override(self, test_override, test_opts):
        search.find_files(opts=test_opts, bin_override=test_override)
        self.mocked_run.assert_called_with(
            [test_override, *test_opts], capture_output=True, text=None
        )

    @given(text())
    def test_directory_override(self, d):
        test_override = "fd_bin"
        test_opts = ["option1", "option2"]
        expected_dir_options = ["--", ".", d]
        search.find_files(opts=test_opts, directory=d, bin_override=test_override)
        self.mocked_run.assert_called_with(
            [test_override, *test_opts, *expected_dir_options],
            capture_output=True,
            text=None,
        )

    def test_default_directory(self):
        test_override = "fd_bin"
        test_opts = ["option1"]
        expected_cmd = [test_override, *test_opts]
        search.find_files(opts=test_opts, bin_override=test_override)
        self.mocked_run.assert_called_with(expected_cmd, capture_output=True, text=None)

    def tearDown(self):
        patch.stopall()


"""Test search.locate_files()
"""


class LocateFiles(unittest.TestCase):
    def setUp(self):
        self.patched_locate_opts = patch(f"{TESTING_MODULE}")
        self.patched_subprocess = patch(f"{TESTING_MODULE}.subprocess.run")

        self.mocked_locate_opts = self.patched_subprocess.start()
        self.mocked_run = self.patched_subprocess.start()

        self.mocked_locate_opts.LOCATE_OPTS = ["opt1", "opt2"]

    @given(p=lists(text()), b=text())
    def test_bin_override(self, p, b):
        search.locate_files(p, bin_override=b)
        self.mocked_run.assert_called_with(
            [b, *self.mocked_locate_opts, *p],
            capture_output=True,
            text=None,
        )

    def tearDown(self):
        patch.stopall()
