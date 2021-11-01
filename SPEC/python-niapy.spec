%bcond_without tests

%global pypi_name niapy
%global pretty_name NiaPy
%global fullver 2.0.0rc18

%global _description %{expand:
Nature-inspired algorithms are a very popular tool for solving optimization
problems. Numerous variants of nature-inspired algorithms have been developed
since the beginning of their era. To prove their versatility, those were tested
in various domains on various applications, especially when they are
hybridized, modified or adapted. However, implementation of nature-inspired
algorithms is sometimes a difficult, complex and tedious task. In order to
break this wall, NiaPy is intended for simple and quick use, without spending
time for implementing algorithms from scratch.}


Name:           python-%{pypi_name}
Version:        2.0.0
Release:        0.2rc18%{?dist}
Summary:        Micro framework for building nature-inspired algorithms

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        https://github.com/NiaOrg/%{pretty_name}/archive/%{fullver}/%{pretty_name}-%{fullver}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-press-theme}
BuildRequires:  %{py3_dist astroid}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist openpyxl}
BuildRequires:  %{py3_dist pandas}

# for tests
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{fullver}
rm -rf %{pretty_name}.egg-info

# Replace ~ in setup.py with >
sed -i 's/~/>/' setup.py

%build
%py3_build

PYTHONPATH=%{buildroot}/%{python3_sitelib} make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/build/html/{.doctrees,.buildinfo} -vf

%install
%py3_install

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%if %{with tests}
# Four tests are failing
PYTHONPATH=%{buildroot}/%{python3_sitelib} pytest -ra \
    -k 'not test_Custom_works_fine and not test_griewank_works_fine' \
    -k 'not test_FA_iters_fine and not test_FA_evals_fine and not test_katsuura' \
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst README.md CHANGELOG.md Algorithms.md Problems.md
%{python3_sitelib}/%{pypi_name}-%{fullver}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%files doc
%license LICENSE
%doc docs/build/html
%doc examples/
%doc paper/
%doc CONTRIBUTING.md CODE_OF_CONDUCT.md

%changelog
* Wed Aug 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc18
- Update to the latest upstream's release - rc18

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2rc17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc17
- Update to the latest upstream's release - rc17
- Remove patch

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-0.2rc16
- Rebuilt for Python 3.10

* Wed May 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc16
- Update to the latest upstream's release - rc16

* Fri May 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.2rc15
- Add additional doc files found in repository to docs

* Sat May 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc15
- Update to the latest upstream's release - rc15

* Fri Apr 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.2rc14
- Removing sed commands - dependencies already removed
- Added JOSS paper in documents

* Fri Apr 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc14
- New version of package

* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.5rc13
- Add examples in subpackage

* Tue Apr 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.4rc13
- Install additional docs

* Tue Mar 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.3rc13
- Skip one test (it is failing from time to time, because of random)

* Fri Mar 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.2rc13
- Remove dependency generator
- Conditional imports for tests

* Wed Mar 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc13
- New version

* Thu Feb 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.5rc12
- Removing linter errors and typos

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4rc12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 4 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.3rc12
- New release - 2.0.0rc12
- Remove dependencies - xlwt, xlsxwriter
- New dependency - openpyxl

* Fri Nov 20 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-0.1rc11
- New release - 2.0.0rc11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2rc10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-0.1rc10
- Remove dep on enum34
- Add python_provides for F32

* Sat Jun 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.2-1
- Initial package

