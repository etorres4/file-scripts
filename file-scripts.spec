#
# spec file for package file-scripts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.9
Release:        0
Summary:        Eric's helper scripts
License:        GPL-3.0-only
Group:          Productivity/File utilities
Source:         %{name}-%{version}.tar.gz
Requires:       %{_bindir}/python3
Requires::      fd
Recommends:     fzf
Supplements:    bash
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

%install
# Install scripts in /usr/bin first
SCRIPTDIR='%{buildroot}%{_bindir}'

for script in *.{py,sh}; do
    install -Dm755 "${script}" "${SCRIPTDIR}/${script%.*}"
done

# Install zsh plugins
ZSHPLUGINDIR='%{buildroot}%{_datadir}/zsh/plugins/helper-scripts'
mkdir -p "${ZSHPLUGINDIR}"
cp zsh/plugins/* "${ZSHPLUGINDIR}"

# Install zsh completion functions
ZSHCOMPLETIONDIR="%{buildroot}%{_datadir}/zsh/site-functions"
mkdir -p "${ZSHCOMPLETIONDIR}"

cp zsh/completions/* "${ZSHCOMPLETIONDIR}"

%check

%files
%attr(0755,-,-) %{_bindir}/*

%files zsh-plugins
%{_datadir}/zsh/plugins/helper-scripts/*
%{_datadir}/zsh/site-functions/*

%changelog
