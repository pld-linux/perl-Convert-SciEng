%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	SciEng
Summary:	Convert::SciEng perl module
Summary(pl):	Modu� perla Convert::SciEng
Name:		perl-Convert-SciEng
Version:	0.90
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::SciEng converts 'numbers' with scientific postfixes to real
numbers, i.e. 2.5u --> 2.5e-6 25K --> 2.5e4

%description -l pl
Convert::SciEng konwertuje 'liczby' z naukowymi ko�c�wkami na prawdziwe
liczby, np.: 2.5u --> 2.5e-6 25K --> 2.5e4

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Convert/SciEng.pm
%{perl_vendorlib}/Convert/demo.pl
%{_mandir}/man3/*
