Various scripts for performing file-related operations such as editing
and deleting.

Q: Why is this simple script written as a Python 3.7+ library? A: I can
reuse the functions across multiple scripts and changes to the
underlying programs can be accounted for in only their respective
modules.

# Requirements
-   fd
-   fzf
-   mlocate
-   python \>= 3.7
-   python-termcolor

# Build Requirements
-   python \>= 3.7
-   pytest
-   python-hypothesis
-   python-sphinx
