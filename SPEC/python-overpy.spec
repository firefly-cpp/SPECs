%global github_name python-overpy
%global pretty_name overpy

%global _description %{expand:
overpy is a wrapper written in Python to access the Overpass API.}

Name:           python-%{pretty_name}
Version:        0.6
Release:        4%{?dist}
Summary:        Python Wrapper to access the Overpass API
License:        MIT
URL:            https://github.com/DinoTools/python-overpy
Source0:        %{url}/archive/%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

#for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-hypothesis

#for docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)

%description -n python3-%{pretty_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{github_name}-%{version}
rm -rf %{pretty_name}.egg-info

%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst CHANGELOG.rst examples/
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%files -n python-%{pretty_name}-doc
%license LICENSE
%doc html/

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-2
- Rebuilt for Python 3.10

* Sat May 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6-1
- Initial package
