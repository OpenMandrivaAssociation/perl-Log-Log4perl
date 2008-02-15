%define	module	Log-Log4perl
%define	name	perl-%{module}
%define version 1.15
%define release %mkrel 1

%define _requires_exceptions perl\(Log::Dispatch::FileRotate\)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Log4j implementation for Perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Log/%{module}-%{version}.tar.bz2
Requires:	perl-Log-Dispatch >= 2.00
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-Log-Dispatch >= 2.00
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
%{module} module for perl.  It provides a powerful logging API to your
application.  Log::Log4perl lets you remote-control and fine-tune the
logging behaviour of your system from the outside. It implements the
widely popular (Java-based) Log4j logging package in pure Perl.

%prep
%setup -q -n %{module}-%{version}
find lib -type f -exec chmod 644 {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README xml eg
%{perl_vendorlib}/Log
%{_mandir}/man3/*

