%define	upstream_name	 Log-Log4perl
%define upstream_version 1.29

%define _requires_exceptions perl\(Log::Dispatch::FileRotate\)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Log4j implementation for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-Log-Dispatch >= 2.00
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-Log-Dispatch >= 2.00

%description
%{upstream_name} module for perl.  It provides a powerful logging API to your
application.  Log::Log4perl lets you remote-control and fine-tune the
logging behaviour of your system from the outside. It implements the
widely popular (Java-based) Log4j logging package in pure Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{_bindir}/l4p-tmpl
%{perl_vendorlib}/Log
%{_mandir}/man1/*
%{_mandir}/man3/*
