%bcond_without tests

%global pypi_name pyqt-feedback-flow

%global _description %{expand:
This is a very simple module for showing simple notifications during the
cycling training sessions in order to pass on a cyclist`s essential
information, as well as information that can be submitted by a sport trainer.
This software allows us to show notification in the realm of a text or a
picture. It was shown that flowing feedback is more appropriate for
a cyclist than static notification or pop up windows. It can also be
integrated into existing PyQt projects very easily.}

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        3%{?dist}
Summary:        Show feedbacks in toast-like notifications

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# The “python3dist(pyqt5)” dependency generated from “PyQt5” in pyproject.toml
# is satisfied by python3-qt5-base, but this project uses PyQt5.QtSvg, which is
# packaged along with other “non-core” modules in python3-qt5. Since this is
# not represented (and currently cannot be represented) in the Python metadata,
# we need explicit BuildRequires *and* Requires on the full python3-qt5.
BuildRequires:  python3-qt5

BuildRequires:  %{py3_dist toml-adapt}
BuildRequires:  %{py3_dist pytest}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

# See the comment on the corresponding BuildRequires.
Requires:       python3-qt5

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep emoji -ver X
toml-adapt -path pyproject.toml -a change -dep PyQt5 -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyqt_feedback_flow

%check
%if %{with tests}
# use smoke test
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md

%changelog
* Thu Mar 10 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.5-3
- Add explicit python3-qt5 dependency for QtSvg

* Thu Mar 10 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.5-2
- Re-enable tests

* Wed Mar 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.5-1
- Update to the latest release

* Wed Feb 16 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Update to the latest release

* Wed Feb 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.3-1
- Update to the latest release

* Tue Feb 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-3
- Do not check imports

* Tue Feb 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-2
- Fix dependency

* Tue Feb 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-1
- Update to the latest release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.1-1
- Initial package
