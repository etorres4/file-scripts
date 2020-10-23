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
    pass


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
        raise FZFError(error.NO_FILE_SELECTED_MESSAGE) from e
    else:
        return Path(selected_file.stdout.decode(LOCALE).strip("\x00"))
