%bcond_with check

%global packname arules
%global ver 1.6
%global packrel 8

%global _description %{expand:
Provides the infrastructure for representing, manipulating and analyzing 
transaction data and patterns (frequent itemsets and association rules). 
Also provides C implementations of the association mining algorithms 
Apriori and Eclat. Hahsler, Gruen and Hornik (2005) 
<doi:10.18637/jss.v014.i15>.}

Name:             R-%{packname}
Version:          1.6.8
Release:          3%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
License:          GPLv3
URL:              https://cran.r-project.org/web/packages/arules/index.html
Summary:          Mining Association Rules and Frequent Itemsets
Source1:          https://github.com/mhahsler/arules/raw/master/LICENSE

BuildRequires:    R-devel, tex(latex)
%if %{with check}
BuildRequires:    R-XML
BuildRequires:    R-testthat
%endif
BuildRequires:    gcc-c++

Requires:         R-core

%description %_description

%prep
%setup -q -c -n %{packname}
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

# we skip only examples (one example suggests pmml which is missing)
%check
%if %{with check}
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes --no-examples %{packname}
%endif

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS.md
%doc %{_libdir}/R/library/%{packname}/CITATION
%license LICENSE
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/libs

%changelog
* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 7 2021 Tom Callaway <spot@fedoraproject.org> - 1.6.8-1
- update to 1.6.8
- rebuild for R 4.1.0

* Mon Apr 5 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.7-2
- New version

* Wed Mar 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.6-2
- Added LICENSE from upstream's repo

* Tue Mar 16 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.6-1
- Enable tests

* Thu Feb 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.6-1
- Initial package creation
