%bcond_without tests

%global pypi_name dotmap

%global _description %{expand:
DotMap is a dot-access dict subclass that has dynamic hierarchy
creation (autovivification), can be initialized with keys, easily
initializes from dict, easily converts to dict, is ordered by insertion.
The key feature is exactly what you want: dot-access.}


Name:           python-%{pypi_name}
Version:        1.3.26
Release:        2%{?dist}
Summary:        Dot access dictionary with dynamic hierarchy creation and ordered iteration

License:        MIT
URL:            https://github.com/drgrib/%{pypi_name}
Source0:        %{pypi_source}

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dotmap

%check
%if %{with tests}
python3 -m unittest
%endif

%files -n python3-dotmap -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.26-1
- Initial package
