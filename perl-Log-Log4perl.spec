%define	upstream_name	 Log-Log4perl
%define upstream_version 1.49

%global __requires_exclude ^perl\\((Sysadm::Install|Log::Dispatch::FileRotate|DBI|RRDs)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Log4j implementation for Perl

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Log-Dispatch >= 2.00
BuildArch:	noarch
Requires:	perl-Log-Dispatch >= 2.00
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
Log::Log4perl lets you remote-control and fine-tune the logging behaviour of
your system from the outside. It implements the widely popular (Java-based)
Log4j logging package in pure Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find lib -type f -exec chmod 644 {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
sed -i -e 's,/usr/local,%{_prefix},g' Makefile t/*.t eg/newsyslog-test eg/benchmarks/simple
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README xml eg
%{_bindir}/l4p-tmpl
%{perl_vendorlib}/Log
%{_mandir}/man1/*
%{_mandir}/man3/*


