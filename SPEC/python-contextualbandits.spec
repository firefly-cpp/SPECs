%global pypi_name contextualbandits
%global download_name david-cortes-contextualbandits-0.1.3.1-157-g8c935a2
%global extract_name david-cortes-contextualbandits-8c935a2

%global _description %{expand:
This Python package contains implementations of methods from different papers
dealing with contextual bandit problems, as well as adaptations from typical
multi-armed bandits strategies. It aims to provide an easy way to prototype
and compare ideas, to reproduce research papers that don't provide 
easily-available implementations of their proposed algorithms, and to
serve as a guide in learning about contextual bandits.}

%global commit          d4eb6597c8ab0b6a249d7fd62928a6c0830fe1d0
%global snapshotdate    20211228
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.3.17
Release:        3%{?dist}
Summary:        Python implementations of algorithms for contextual bandits

License:        BSD
URL:            https://github.com/david-cortes/contextualbandits

# we fetch the latest tarball from the upstream
# we do not rely on Pypi version (no docs, no LICENSE included)
Source0:        %url/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Cython

# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{commit}
rm -rf %{pypi_name}.egg-info
# remove toml file. It is actually not used in real build.
rm -rf pyproject.toml

%generate_buildrequires
echo 'python3dist(numpy)'
echo 'python3dist(scipy)'
echo 'python3dist(pandas)'
echo 'python3dist(scikit-learn)'
echo 'python3dist(joblib)'

%build
%pyproject_wheel

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%files doc
%license LICENSE
%doc html/
%doc example/

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 3 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.17-2
- Port to pyproject-rpm-macros

* Sat Jan 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.17-1
- Update to the latest upstream's release
- Remove patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.14-2
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.14-1
- Initial package
