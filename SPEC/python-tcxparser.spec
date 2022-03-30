%bcond_without tests

%global pretty_name tcxparser
%global pypi_name python-%{pretty_name}
%global extract_name python_tcxparser

%global _description %{expand:
python-tcxparser is a minimal parser for Garmin's TCX file format. It is not in
any way exhaustive. It extracts just enough data to show the most important
attributes of sport activity.}

Name:           python-%{pretty_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Tcxparser is a minimal parser for Garmin TCX file format

License:        BSD
URL:            https://github.com/vkurup/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist lxml}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pretty_name}

%check
%{python3} setup.py test

%files -n python3-%{pretty_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst AUTHORS.rst CHANGES.rst

%changelog
* Sun Jan 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-1
- New version of software - 2.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-2
- Use pyproject rpm macros

* Thu Dec 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-1
- New version of software - 2.1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Tue May 4 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-2
- Install additional docs

* Sun Feb 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-1
- New version - 2.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-2
- Same dependencies removed

* Sat Nov 14 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package
