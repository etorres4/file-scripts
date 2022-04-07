"""
.. moduleauthor:: Eric Torres
.. module:: package.module
    :synopsis: Short and succinct module description
"""
# ========== Imports ==========
import shutil
import subprocess

from sys import platform

# ========== Constants ==========
# ----- Commands -----
# Options: show hidden files, null terminator, files only
# Optional arguments: show vcs files, show every file
FIND_CMD = shutil.which("fd")
DEFAULT_FIND_OPTS = [
    "--hidden",
    "--print0",
    "--type",
    "f",
    "--type",
    "l",
]
EXTRA_FIND_OPTS = {"no_ignore": "--no-ignore", "no_ignore_vcs": "--no-ignore-vcs"}

# Options: null terminator, ignore case, print names matching all non-option arguments
LOCATE_CMD = shutil.which("locate")

# Platform-specific options
# macOS doesn't support GNU-style long options
LOCATE_OPTS = []
if platform == "linux":
    LOCATE_OPTS = ["--all", "--ignore-case", "--null"]
elif platform == "darwin":
    LOCATE_OPTS = ["-0", "-i"]

# ========== Functions ==========
def find_files(
    *,
    opts=DEFAULT_FIND_OPTS,
    directory=None,
    capture_text=None,
    bin_override=None,
    pattern=None,
):
    """Use a find-based program to locate files. The returned data is
    the stdout of the completed process.

    :param opts: options to pass to the find program
    :type opts: list of str
    :param directory: directory to search for files
    :type directory: str
    :param capture_text: capture output as text
    :type capture_text: bool
    :param bin_override: override find binary
    :type bin_override: str
    :param pattern: patterns to pass to fd
    :type pattern: str
    :returns: path of user-selected file
    :rtype: bytes, str if capture_text was initialized from None
    """

    # Sample of a command that gets passed to subprocess:
    # ['/usr/bin/find', '--hidden', '--', '<pattern>', 'path/to/directory']
    cmd = [bin_override if bin_override is not None else FIND_CMD, *opts]

    cmd.append("--")

    """ Options Matrix
      pattern    T T F F
      directory  T F T F
                 1 2 3 4

      1. Pattern and directory were given: pass both
      2. Only pattern was given: pass pattern and give . as directory
      3. Only directory was given: pass . as pattern and give directory
      4. Neither pattern nor directory were given: do nothing
    """
    if pattern is not None and directory is not None:
        cmd.extend([pattern, directory])
    elif pattern is not None and directory is None:
        cmd.extend([pattern, "."])
    elif pattern is None and directory is not None:
        cmd.extend([".", directory])
    elif pattern is None and directory is None:
        pass

    return subprocess.run(cmd, capture_output=True, text=capture_text).stdout


def locate_files(patterns, *, bin_override=None, capture_text=None):
    """Use a locate-based program to locate files, then pass to fzf.

    :param patterns: patterns to pass to locate
    :type patterns: list
    :param bin_override: override find binary
    :type bin_override: str
    :param capture_text: capture output as text
    :type capture_text: bool
    :returns: path of user-selected file
    :rtype: bytes, str if capture_text was initialized from None
    """
    cmd = [bin_override if bin_override is not None else LOCATE_CMD, *LOCATE_OPTS, "--"]
    cmd.extend(patterns)

    return subprocess.run(cmd, capture_output=True, text=capture_text).stdout
