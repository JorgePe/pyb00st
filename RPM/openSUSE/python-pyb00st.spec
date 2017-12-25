#
# spec file for package python-pyb00st
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define pypi_name pyb00st
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-%{pypi_name}
Version:        0.0.0
Release:        0
Summary:        Python for LEGO BOOST
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/JorgePe/pyb00st
Source:         %{pypi_name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  python3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       python3

%python_subpackages

%description
The LEGO BOOST Move Hub is a BLE (Bluetooth Low Energy) device like the LEGO WeDo 2.0 Smart Hub
 and the Vengit SBrick which I already managed to control with the LEGO MINDSTORMS EV3 thanks to
 [pygattlib](https://bitbucket.org/OscarAcena/pygattlib), a python library for BLE.

I've been [reverse engineering the LEGO BOOST](https://github.com/JorgePe/BOOSTreveng) Move Hub
 and since I'm now officially crazy I decided to try to write a python package.

I started this project with pygattlib. It's a library that makes direct use of BlueZ and has been
 included in pybluez. But since python3 version of pygattlib has problems with notifications I
  started to use a different library, [pygatt](https://github.com/peplin/pygatt/tree/master/pygatt),
  that doesn't make direct use of Bluez - instead, it makes use of a *backend*. On linux systems
  this backend can be BlueZ (through system calls to BlueZ commands like hcitool and gattool) but on
  other systems (and probably also on linux aswell) it uses a different backend, based on BlueGiga's
  API - so a BG adapter, like BLED112, is needed.

Why did I call it pyb00st? Well, boost is a C++ library and there are already lots of python libraries
 related to it and I don't want to add the LEGO word because I don't want troubles.

By the way...


%prep
%setup -q -n %{pypi_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/pyb00st

%files  %{python_files}
%defattr(-,root,root)
%doc README.md
%{python_sitelib}/*

%changelog

