%bcond_with tests

%global pypi_name sport-activities-features
%global pretty_name sport_activities_features

%global _description %{expand:
A minimalistic toolbox for extracting features 
from sport activity files written in Python. Proposed software 
supports the extraction of following topographic features from
sport activity files: number of hills, average altitude of identified 
hills, total distance of identified hills, climbing ratio (total distance
of identified hills vs. total distance), average ascent of hills, 
total ascent, total descent and many others.}

Name:           python-%{pypi_name}
Version:        0.2.7
Release:        1%{?dist}
Summary:        A toolbox for extracting features from sport activity files 

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  make

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{py3_dist toml-adapt} 

#For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -S git
rm -fv poetry.lock

#make dependencies consistent with Fedora versions
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

#remove package geotiler (not yet ported to Fedora)
toml-adapt -path pyproject.toml -a remove -dep geotiler -ver 0.1.0

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files sport_activities_features

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/LICENSE
rm -rf %{buildroot}/%{python3_sitelib}/CHANGELOG.md

%check	
%if %{with tests}
%pytest -k 'not test_data_analysis'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%files doc
%license LICENSE
%doc docs/_build/html
%doc examples/

%changelog
* Wed Oct 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.7-1
- Update to the latest upstream's release

* Sat Oct 16 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.6-2
- Disable tests for now (one dependency is missing)

* Sat Oct 16 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.6-1
- Update to the latest upstream's release

* Fri Sep 24 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.5-1
- Update to the latest upstream release

* Fri Sep 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-2
- Remove hardcoded dependencies

* Sun Aug 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Update to the latest upstream release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.3-1
- Update to the latest upstream release

* Tue Jul 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.2-1
- Update to the latest upstream release

* Thu Jul 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- Update to the latest upstream release

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-6
- Minor corrections

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-5
- Skip one test

* Mon Jun 28 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-4
- Corrections (new version of deps became available)

* Wed Jun 9 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-3
- Minor corrections

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.10

* Wed May 12 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-1
- Update to the latest upstream release

* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-2
- Install additional files

* Thu Apr 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-1
- Initial package
