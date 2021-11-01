%global pretty_name FireflyAlgorithm

%global _description %{expand:
Implementation of Firefly Algorithm (FA) for optimization.}

Name:           python-%{pretty_name}
Version:        0.0.4
Release:        1%{?dist}
Summary:        Firefly Algorithm in Python

License:        MIT
URL:            https://github.com/firefly-cpp/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%pycached %{python3_sitelib}/%{pretty_name}.py

%changelog
* Wed Feb 3 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.4-1
- New version - 0.0.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.2-1
- New version - 0.0.2

* Fri Nov 20 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.1-1
- Initial package
