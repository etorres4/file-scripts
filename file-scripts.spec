#
# spec file for package file-scripts
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.0.0
Release:        0
Summary:        Set of scripts for manipulating files
License:        GPL-3.0-only
Group:          Productivity/File utilities
URL:            https://github.com/etorres4/file-scripts
Source:         %{name}-%{version}.tar.gz
Requires:       /usr/bin/bash
Requires:       fd
Requires:       fzf
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

%install
for script in bin/*; do
    install -Dm755 "$script" "%{buildroot}/usr/bin/$(basename script)"
done

# Install zsh completion functions
ZSHCOMPLETIONDIR="%{buildroot}%{_datadir}/zsh/site-functions"
mkdir -p "${ZSHCOMPLETIONDIR}"

for completion in zsh/*; do
    install -Dm644 "${completion}" "${ZSHCOMPLETIONDIR}/${completion##*.}"
done

%files
%attr(0755,-,-) %{_bindir}/*

%files zsh-plugins
%{_datadir}/zsh/
%{_datadir}/zsh/site-functions

%changelog
