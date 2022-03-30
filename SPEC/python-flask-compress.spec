%global pypi_name flask-compress

%global _description %{expand:
Flask-Compress allows you to easily compress your Flask application's
responses with gzip.

The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.}

Name:           python-%{pypi_name}
Version:        1.11
Release:        1%{?dist}
Summary:        Compress responses in your Flask app with gzip or brotli

License:        MIT
URL:            https://github.com/colour-science/flask-compress
Source0:        %{pypi_source Flask-Compress}
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(tox)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(brotli)
Requires:       python3dist(flask)
%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n Flask-Compress-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_compress

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
* Tue Mar 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.11-1
- New upstream's release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.10.1-4
- Use pyproject-rpm-project

* Mon Dec 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.10.1-3
- Use macro for descriptions

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Rafael Fontenelle <rafaelff@gnome.org> - 1.10.1-1
- Update to 1.10.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Rafael Fontenelle <rafaelff@gnome.org> - 1.7.0-1
- Update to 1.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Rafael Fontenelle <rafaelff@gnome.org> - 1.5.0-2
- use macro for source0

* Tue May 12 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.0-1
- Initial package.
