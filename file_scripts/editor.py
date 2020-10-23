"""
.. moduleauthor:: Eric Torres
.. module:: file_scripts.editor
    :synopsis: Helper functions for interacting with system editors
"""
# ========== Imports ==========
import os
import shutil

from pathlib import Path

# ========== Constants ==========
SUDO_COMMAND = "sudo"

# ========== Functions ==========
def select_editor(override=None):
    """Return a canonical path to an editor.

    Select an editor from one of:
    * -e, --editor
    * $EDITOR
    * Default of vim

    In this order

    If an editor cannot be resolved, then a FileNotFoundError is raised instead.

    :param override: argument to override an editor
    :returns: path to one of these editors
    :rtype: str
    :raises: FileNotFoundError if an editor could not be resolved
    """
    editor = None

    if override is not None:
        editor = shutil.which(override)
    elif "EDITOR" in os.environ:
        editor = shutil.which(os.environ.get("EDITOR"))
    elif shutil.which("vim") is not None:
        editor = shutil.which("vim")

    if editor is None:
        raise FileNotFoundError("An editor could not be resolved")

    return editor


def gen_editor_cmd(editor, filename):
    """Generate a command line to run for editing a file based on
    permissions. This command line is suitable for passing to
    subprocess.run().

    This command does not pass extra options to the editor, hence
    there are no arguments to pass for options.

    Conditions
    ----------
    * Path exists: use normal command
    * Path does not exist: use normal command
    * Path exists but is not readable by current process: use SUDO_COMMAND


    :param editor: path of editor
    :type editor: str or path-like object
    :param filename: path/name of file to edit
    :type filename: str or path-like object
    :returns: command to execute to edit file
    :rtype: list
    """
    # Possible for a race condition to occur here
    # What happens if the file or its metadata changes?
    path = Path(filename)
    if path.exists() and not os.access(path, os.W_OK):
        return [SUDO_COMMAND, "--edit", filename]
    else:
        return [editor, filename]
