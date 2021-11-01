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

%global commit          8c935a254129050ca7355f4d1ec5608bcdcd3bb5
%global snapshotdate    20210419
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.3.14
Release:        3%{?dist}
Summary:        Python Implementations of Algorithms for Contextual Bandits

License:        BSD
URL:            https://github.com/david-cortes/contextualbandits

# we fetch the latest tarball from the upstream
# we do not rely on Pypi version (no docs, no LICENSE included)
Source0:        %url/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz

# we remove -march=native option which is not supported on powerpc 
Patch0:         0001-Remove-Compile-Flags-for-contextualbandits.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Cython

# For the patch
BuildRequires:  git-core

#package specific BRs
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(joblib)

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

%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc html/
%doc example/

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.14-2
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.14-1
- Initial package
