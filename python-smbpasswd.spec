Summary:	Python SMB Password Hash Generator Module
Name:		python-smbpasswd
Version:	1.0.1
Release:	5
Group:		Development/Python
License:	GPLv2
Url:		http://barryp.org/software/py-smbpasswd
Source0:	py-smbpasswd-%{version}.tar.gz
BuildRequires:	pkgconfig(python)

%description
This package contains a python module, which is able to generate LANMAN and
NT password hashes suiteable to us with Samba.

%prep
%setup -qn py-smbpasswd-%{version}

%build
CFLAGS="%{optflags}" 
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc COPYING README.txt
%{py_platsitedir}/smbpasswd.so
%{py_platsitedir}/*egg-info

