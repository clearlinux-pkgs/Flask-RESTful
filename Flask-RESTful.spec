#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Flask-RESTful
Version  : 0.3.8
Release  : 21
URL      : https://files.pythonhosted.org/packages/67/65/84f3218666fc115497a13ff727f16d02374d07d1924cd4fd72e275294e8b/Flask-RESTful-0.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/67/65/84f3218666fc115497a13ff727f16d02374d07d1924cd4fd72e275294e8b/Flask-RESTful-0.3.8.tar.gz
Summary  : Simple framework for creating REST APIs
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Flask-RESTful-license = %{version}-%{release}
Requires: Flask-RESTful-python = %{version}-%{release}
Requires: Flask-RESTful-python3 = %{version}-%{release}
Requires: Flask
Requires: aniso8601
Requires: pytz
Requires: six
BuildRequires : Flask
BuildRequires : aniso8601
BuildRequires : blinker
BuildRequires : buildreq-distutils3
BuildRequires : python-mock
BuildRequires : pytz
BuildRequires : six

%description
# Flask-RESTful
[![Build Status](https://travis-ci.org/flask-restful/flask-restful.svg?branch=master)](http://travis-ci.org/flask-restful/flask-restful)
[![Coverage Status](http://img.shields.io/coveralls/flask-restful/flask-restful/master.svg)](https://coveralls.io/r/flask-restful/flask-restful)
[![PyPI Version](http://img.shields.io/pypi/v/Flask-RESTful.svg)](https://pypi.python.org/pypi/Flask-RESTful)

%package license
Summary: license components for the Flask-RESTful package.
Group: Default

%description license
license components for the Flask-RESTful package.


%package python
Summary: python components for the Flask-RESTful package.
Group: Default
Requires: Flask-RESTful-python3 = %{version}-%{release}
Provides: flask-restful-python

%description python
python components for the Flask-RESTful package.


%package python3
Summary: python3 components for the Flask-RESTful package.
Group: Default
Requires: python3-core
Provides: pypi(flask_restful)
Requires: pypi(aniso8601)
Requires: pypi(flask)
Requires: pypi(pytz)
Requires: pypi(six)

%description python3
python3 components for the Flask-RESTful package.


%prep
%setup -q -n Flask-RESTful-0.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586396727
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Flask-RESTful
cp %{_builddir}/Flask-RESTful-0.3.8/LICENSE %{buildroot}/usr/share/package-licenses/Flask-RESTful/25e57572adbfec461a37a7b37592700747a2aea9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Flask-RESTful/25e57572adbfec461a37a7b37592700747a2aea9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
