%global pypi_name EvoPreprocess
%global simple_name evopreprocess


%global _description %{expand:
EvoPreprocess is a Python toolkit for sampling datasets, instance weighting,
and feature selection. It is compatible with scikit-learn and 
imbalanced-learn packages. It is based on the NiaPy library for the 
implementation of nature-inspired algorithms.}

Name:           python-%{pypi_name}
Version:        0.4.3
Release:        1%{?dist}
Summary:        A Python Toolkit for Data Preprocessing 
License:        GPLv3
URL:            https://github.com/karakatic/%{pypi_name}
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
            
BuildArch:      noarch

BuildRequires:  python3-devel

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
# No setup.cfg, tox.ini or pyproject.toml
echo 'python3dist(pip)'
echo 'python3dist(packaging)'
echo 'python3dist(setuptools)'
echo 'python3dist(wheel)'
echo 'python3dist(numpy)'
echo 'python3dist(scipy)'
echo 'python3dist(scikit-learn)'
echo 'python3dist(imbalanced-learn)'
echo 'python3dist(niapy)'

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{simple_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md Examples/

%changelog
* Sat Oct 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.3-1
- Update to the latest upstream's release

* Fri Oct 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-6
- Reconcile niapy version with patch

* Sun Sep 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-5
- Remove patch

* Sat Sep 25 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-4
- Use python rpm macros

* Fri Sep 3 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-3
- Patch dependencies

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-1
- Update to the latest upstream's release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.4-5
- Rebuilt for Python 3.10

* Mon May 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-4
- Removing some macros
- Install examples

* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-3
- Removing dependency generator
- Description fixes
- BuildArch set to noarch
- Fresh rebuilt

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-1
- Initial package
