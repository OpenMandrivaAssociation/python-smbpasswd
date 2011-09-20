Name:           python-smbpasswd
Version:        1.0.1
Release:        1
Summary:        Python SMB Password Hash Generator Module

Group:          Development/Python
License:        GPLv2
URL:            http://barryp.org/software/py-smbpasswd
Source0:        py-smbpasswd-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel

%description
This package contains a python module, which is able to generate LANMAN and
NT password hashes suiteable to us with Samba.

%prep
%setup -q -n py-smbpasswd-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" 
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_platsitedir}/smbpasswd.so
%{py_platsitedir}/*egg-info
%doc COPYING README.txt
