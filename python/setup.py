import setuptools
from sphinx.setup_command import BuildDoc

# ========== Constants ==========
EXCLUDED_PACKAGES = ["test", "tests"]
PACKAGES = setuptools.find_packages(exclude=EXCLUDED_PACKAGES)
DEPENDENCIES = ["termcolor"]
SCRIPTS = ["bin/fedit", "bin/cptemplate", "bin/quickdel"]
CMDCLASS = {"build_sphinx": BuildDoc}

# ========== Functions ==========
with open("README", "r") as fh:
    long_description = fh.read()

# ========== Package Setup ==========
setuptools.setup(
    name="file_scripts",
    version="2.0.0",
    author="Eric Torres",
    author_email="eric.torres@its-et.me",
    description="File-related helper scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/etorres4/file-scripts",
    packages=PACKAGES,
    scripts=SCRIPTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    command_options={
        "build_sphinx": {
            "project": ("setup.py", "name"),
            "version": ("setup.py", "version"),
            "release": ("setup.py", "release"),
            "source_dir": ("setup.py", "doc"),
        }
    },
)
