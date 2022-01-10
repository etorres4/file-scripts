"""
.. moduleauthor:: Eric Torres
.. module:: files-scripts.fzf
    :synopsis: Helper functions for interacting with fzf
"""
# ========== Imports ==========
import shutil
import subprocess

import file_scripts.error as error

from pathlib import Path

# ========== Constants ==========
# ----- Commands -----
# Options: read null terminator, auto-select if one option, exit if no options, print null terminator
FZF_CMD = shutil.which("fzf")
FZF_OPTS = ["--read0", "--select-1", "--exit-0", "--print0"]

# ----- Misc. -----
LOCALE = "utf-8"


class FZFError(Exception):
    """Custom error class for any errors that occur when fzf is run.

    **Attributes**

    * exit_code: exit code when fzf exited
    * message: stderr of fzf's process when the error occured

    """

    def __init__(self, exit_code):
        """
        :type exit_code: int
        """
        self.exit_code = exit_code

    def __repr__(self):
        return f"FZFError({self.exit_code})"

    def __str__(self):
        return str(__repr__)


# ========== Functions ==========
def select_file_with_fzf(files):
    """Run fzf on a stream of searched files for the user to select.

    :param files: stream of null-terminated files to read
    :type files: bytes stream (stdout of a completed process)
    :returns: selected file
    :rtype: path-like object
    :raises: FZFError if there was an error with fzf or no file was selected
    """
    output = subprocess.run([FZF_CMD, *FZF_OPTS], input=files, stdout=subprocess.PIPE)

    try:
        output.check_returncode()
    except subprocess.CalledProcessError as e:
        raise FZFError(e.returncode) from e
    else:
        return Path(output.stdout.decode(LOCALE).strip("\x00"))
