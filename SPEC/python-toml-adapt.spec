%bcond_without tests

%global original_name toml-adapt
%global pretty_name toml_adapt

%global _description %{expand:
This is a very simple cli for manipulating toml files.}

Name:           python-%{original_name}
Version:        0.1.6
Release:        1%{?dist}
Summary:        Adapt toml files

License:        MIT
URL:            https://github.com/firefly-cpp/%{original_name}
Source0:        %{url}/archive/%{version}/%{original_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{original_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{original_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{original_name}-%{version}
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pretty_name}

install -D -t '%{buildroot}%{_mandir}/man1' -m 0644 %{original_name}.1

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{original_name} -f %{pyproject_files}
%{_bindir}/%{original_name}
%license LICENSE
%doc README.md
%{_mandir}/man1/%{original_name}.1*
 
%changelog
* Wed Oct 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.6-1
- Update to the latest release

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.5-1
- Update to the latest release

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Update to the latest release

* Tue Jun 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.3-1
- Update to the latest release

* Wed Jun 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.2-1
- Update to 0.1.2 (fixes man page installed in %%{python3_sitelib})
- Fix permissions on installed man page

* Tue Jun 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.1-1
- Update to the latest release
- Add man page

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.10

* Tue Jun 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.0-1
- Initial package
