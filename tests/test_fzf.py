"""
.. moduleauthor:: Eric Torres
:synopsis: Unit tests for the fzf module.
"""
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

import file_scripts.fzf as fzf

# ========== Constants ==========
TESTING_PACKAGE = "file_scripts"
TESTING_MODULE = f"{TESTING_PACKAGE}.fzf"

# ========== Test Cases ==========
class TestRunFZF(unittest.TestCase):
    def setUp(self):
        self.patched_subprocess = patch(f"{TESTING_MODULE}.subprocess.run")

        self.mocked_run = self.patched_subprocess.start()

    def test_creates_pathlike_object(self):
        self.assertIsInstance(fzf.select_file_with_fzf(b'test'), Path)

    def tearDown(self):
        patch.stopall()
