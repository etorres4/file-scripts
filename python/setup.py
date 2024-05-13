import setuptools
from sphinx.setup_command import BuildDoc

# ========== Constants ==========
EXCLUDED_PACKAGES = ["test", "tests"]
PACKAGES = setuptools.find_packages(exclude=EXCLUDED_PACKAGES)
SCRIPTS = ["bin/fedit", "bin/cptemplate", "bin/quickdel"]
CMDCLASS = {"build_sphinx": BuildDoc}

# ========== Package Setup ==========
setuptools.setup(
    packages=PACKAGES,
    scripts=SCRIPTS,
    command_options={
        "build_sphinx": {
            "project": ("setup.py", "name"),
            "version": ("setup.py", "version"),
            "release": ("setup.py", "release"),
            "source_dir": ("setup.py", "doc"),
        }
    },
)
