%bcond_without check

%global packname pbapply
%global ver 1.4
%global packrel 3

%global _description %{expand:
A lightweight package that adds progress bar to vectorized R functions 
('*apply'). The implementation can easily be added to functions where
showing the progress is useful (e.g. bootstrap). The type and style of
the progress bar (with percentages or remaining time) can be set through
options. Supports several parallel processing backends.}

Name:             R-%{packname}
Version:          %{ver}.%{packrel}
Release:          4%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
License:          GPLv2
URL:              https://cran.rstudio.com/web/packages/pbapply/index.html
Summary:          Adding Progress Bar to '*apply' Functions

BuildRequires:    R-devel, tex(latex)
Requires:         R-core

BuildArch:        noarch

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
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help

%changelog
* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.4.3-2
- Rebuilt for R 4.1.0

* Tue Apr 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.3-1
- Switched to noarch

* Sun Apr 25 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.3-1
- Initial package
