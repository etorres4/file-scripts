#
# spec file for package file-scripts
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           file-scripts
Version:        0.9.2
Release:        0
Summary:        Eric's helper scripts
License:        GPL-3.0-only
Group:          Productivity/File utilities
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3 >= 3.7
BuildRequires:  python3-hypothesis
BuildRequires:  python3-setuptools
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pytest
BuildRequires:  fdupes
Requires:       python3 >= 3.7
Requires:       fd
Requires:       fzf
Requires:       python3-termcolor
Supplements:    zsh
BuildArch:      noarch

%description
A collection of various helper scripts and some shell completions to speed up terminal workflow.

%package zsh-plugins
Summary:        zsh addons for helper scripts
Requires:       %{name} = %{version}
Requires:       /bin/zsh

%description zsh-plugins
Plugins and completions for helper scripts.

%prep
%setup -q

%build
%{python3_build}

%install
%{python3_install}

# Install zsh completion functions
ZSHCOMPLETIONDIR="%{buildroot}%{_datadir}/zsh/site-functions"
mkdir -p "${ZSHCOMPLETIONDIR}"

for completion in zsh/*; do
    install -Dm644 "${completion}" "${ZSHCOMPLETIONDIR}/${completion##*.}"
done

%fdupes %{buildroot}/%{_prefix}

%check
pytest

# %files %%{python_files} (bug)
%files
%attr(0755,-,-) %{_bindir}/*
/usr/lib/python3*/*

%files zsh-plugins
%{_datadir}/zsh/
%{_datadir}/zsh/site-functions

%changelog
