%include	/usr/lib/rpm/macros.perl
Summary:	Convert-SciEng perl module
Summary(pl):	Modu³ perla Convert-SciEng
Name:		perl-Convert-SciEng
Version:	0.90
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-SciEng-%{version}.tar.gz
Patch0:		perl-Convert-SciEng-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-SciEng converts 'numbers' with scientific postfixes to real
numbers, i.e. 2.5u --> 2.5e-6 25K --> 2.5e4

%description -l pl
Convert-SciEng konwertuje 'liczby' z naukowymi koñcówkami na prawdziwe
liczby, np.: 2.5u --> 2.5e-6 25K --> 2.5e4

%prep
%setup -q -n Convert-SciEng-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Convert/SciEng
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Convert/SciEng.pm
%{perl_sitelib}/Convert/demo.pl
%{perl_sitearch}/auto/Convert/SciEng

%{_mandir}/man3/*
