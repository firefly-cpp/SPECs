%bcond_without tests

%global pypi_name pyunicorn

%global _description %{expand:
pyunicorn is a fully object-oriented Python package for the advanced
analysis and modeling of complex networks. Above the standard measures
of complex network theory such as degree, betweenness and clustering 
coefficient it provides some uncommon but interesting statistics like 
Newman's random walk betweenness. pyunicorn features novel node-weighted
(node splitting invariant) network statistics as well as measures 
designed for analyzing networks of interacting/interdependent networks.}

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        4%{?dist}
Summary:        Unified complex network and recurrence analysis toolbox

# The entire source code is BSD except the following files:
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/__init__.py
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/compat.py
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/progressbar.py
#pyunicorn-0.6.1/pyunicorn/utils/progressbar/widgets.py
License:        BSD and LGPLv2+
URL:            http://www.pik-potsdam.de/~donges/pyunicorn/
Source0:        %{pypi_source}
Patch0:         0001-Skip-test.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Cython

BuildRequires:  python3-igraph
BuildRequires:  numpy
BuildRequires:  python3-networkx
BuildRequires:  python3-basemap
BuildRequires:  python3-sphinx
BuildRequires:  python3-scipy

# For the patch
BuildRequires:  git-core

Requires:  matplotlib

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-flake8
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pylint
BuildRequires:  python3-tox
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
for lib in $(find . -name "*.py"); do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%py3_build

%install
%py3_install

# patch intended for skipping two tests due to the failed attempts on i686
%check
%if %{with tests}
tox -e units
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.1-3
- Rebuilt for Python 3.10

* Mon Mar 29 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-2
- New patch - one test is failing on s390x

* Mon Mar 29 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Multiple licences added

* Mon Mar 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Initial package

