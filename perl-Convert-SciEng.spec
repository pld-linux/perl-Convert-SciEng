%define		pdir	Convert
%define		pnam	SciEng
Summary:	Convert::SciEng Perl module - convert 'numbers' with scientific postfixes
Summary(pl.UTF-8):	Moduł Perla Convert::SciEng - konwersja liczb z naukowymi końcówkami
Name:		perl-Convert-SciEng
Version:	0.91
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21f183f91cb184844499927373255ca4
URL:		http://search.cpan.org/dist/Convert-SciEng/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::SciEng converts 'numbers' with scientific postfixes to real
numbers, i.e. 2.5u --> 2.5e-6 25K --> 2.5e4.

%description -l pl.UTF-8
Convert::SciEng konwertuje 'liczby' z naukowymi końcówkami na
prawdziwe liczby, np.: 2.5u --> 2.5e-6 25K --> 2.5e4.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Convert/SciEng.pm
%{perl_vendorlib}/Convert/demo.pl
%{_mandir}/man3/*
