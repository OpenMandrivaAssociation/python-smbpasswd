Name:           python-smbpasswd
Version:        1.0.2
Release:        4
Summary:        Python SMB Password Hash Generator Module

Group:          Development/Python
License:        GPLv2
URL:            http://barryp.org/software/py-smbpasswd
Source0:        smbpasswd-%{version}.tgz
BuildRequires:	python-devel
%rename		py-smbpasswd

%description
This package contains a python module, which is able to generate LANMAN and
NT password hashes suiteable to us with Samba.

%prep
%setup -q -n smbpasswd-%{version}

%build
CFLAGS="%{optflags}" 
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%{py_platsitedir}/smbpasswd.so
%{py_platsitedir}/*egg-info
%doc README.txt
