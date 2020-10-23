import setuptools
from sphinx.setup_command import BuildDoc

# ========== Constants ==========
EXCLUDED_PACKAGES = ["test", "tests"]
PACKAGES = setuptools.find_packages(exclude=EXCLUDED_PACKAGES)
DEPENDENCIES = ["termcolor"]
SCRIPTS = ["bin/fedit", "bin/cptemplate", "bin/quickdel"]
CMDCLASS = {"build_sphinx": BuildDoc}

# ========== Functions ==========
with open("README.rst", "r") as fh:
    long_description = fh.read()

# ========== Package Setup ==========
setuptools.setup(
    name="file_scripts",
    version="0.1.1",
    author="Eric Torres",
    author_email="erictorres4@protonmail.com",
    description="File-related helper scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/pypa/sampleproject",
    packages=PACKAGES,
    scripts=SCRIPTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
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
