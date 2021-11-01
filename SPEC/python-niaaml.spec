%bcond_without tests

%global pypi_name niaaml
%global pretty_name NiaAML

%global _description %{expand:
NiaAML is a framework for Automated Machine Learning based on 
nature-inspired algorithms for optimization. This package uses 
algorithms implementation from NiaPy.}

Name:           python-%{pypi_name}
Version:        1.1.6
Release:        4%{?dist}
Summary:        Python automated machine learning framework

License:        MIT
URL:            https://github.com/lukapecnik/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildRequires:  make

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}
BuildRequires:  %{py3_dist toml-adapt}

#For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%{?python_:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files niaaml

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/LICENSE
rm -rf %{buildroot}/%{python3_sitelib}/CHANGELOG.md

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md COMPONENTS.md CITATION.md

%files doc
%license LICENSE
%doc docs/_build/html
%doc examples/
%doc paper/
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md CITATION.md

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.6-2
- Minor corrections

* Mon Jun 28 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.6-1
- Update to the latest upstream's major release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.5-2
- Rebuilt for Python 3.10

* Wed Jun 2 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.5-1
- Update to the latest release

* Tue May 25 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.4-1
- Update to the latest release

* Fri May 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.2-1
- Update to the latest release
- Remove patch

* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-4
- Install additional files

* Thu Apr 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-3
- Minor corrections (path)

* Mon Mar 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-2
- Enable tests

* Tue Mar 9 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.1-1
- New version - 1.1.1

* Wed Mar 3 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-3
- Add make dependency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package
