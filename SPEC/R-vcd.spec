%bcond_without check

%global packname vcd
%global ver 1.4
%global packrel 8

%global _description %{expand:
Visualization techniques, data sets, summary and inference procedures aimed
particularly at categorical data. Special emphasis is given to highly
extensible grid graphics. The package was package was originally inspired
by the book "Visualizing Categorical Data" by Michael Friendly and is now
the main support package for a new book, "Discrete Data Analysis with R"
by Michael Friendly and David Meyer (2015).}

Name:             R-%{packname}
Version:          %{ver}.%{packrel}
Release:          3%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
License:          GPLv2
URL:              https://cran.r-project.org/web/packages/vcd/index.html
Summary:          Visualizing categorical data

BuildRequires:    R-devel, tex(latex)
BuildRequires:    R-colorspace
BuildRequires:    R-lmtest

BuildArch:        noarch

Requires:         R-core

%description %_description

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
%if %{with check}
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes --no-tests %{packname}
%endif

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/CITATION
%doc %{_datadir}/R/library/%{packname}/NEWS.Rd
%doc %{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/demo


%changelog
* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.8-2
- Rebuilt for R 4.1.0

* Sun May 2 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.8-1
- Initial package
