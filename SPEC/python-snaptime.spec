%bcond_without tests

%global pretty_name snaptime
%global commit          cc8b7d4489ee8104b717ed461dd21aee806ae322
%global snapshotdate    20210420
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global _description %{expand:
The snaptime package is about transforming timestamps simply.}

Name:           python-%{pretty_name}
Version:        0.2.4
Release:        8%{?dist}
Summary:        Transforming timestamps simply

License:        MIT
URL:            https://github.com/zartstrom/snaptime
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{commit}

%build
%py3_build

%install
%py3_install

%check
#skipping three tests
%if %{with tests}
%pytest -k 'not test_bad_weekday and not test_parse_error and not test_unit_error'
%endif

%files -n python3-%{pretty_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%pycached %{python3_sitelib}/%{pretty_name}/main.py
%pycached %{python3_sitelib}/%{pretty_name}/__init__.py

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-6
- Switch to pytest macro

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.4-5
- Rebuilt for Python 3.10

* Tue Apr 20 15:11:26 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.4-4
- Target a specific commit instead of the master git tip

* Wed Mar 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-3
- Cosmetic changes

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Initial package
