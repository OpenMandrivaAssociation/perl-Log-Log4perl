%define	upstream_name	 Log-Log4perl
%define upstream_version 1.42

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Sysadm::Install\\)|perl\\(Log::Dispatch::FileRotate\\)|perl\\(DBI(.*)\\)|perl\\(RRDs(.*)\\)'
%else
%define _requires_exceptions perl\(\\(Log::Dispatch::FileRotate\\|DBI\\|RRDs\\)\)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	Log4j implementation for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Log4perl-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Log-Dispatch >= 2.00
BuildArch:	noarch
Requires:	perl-Log-Dispatch >= 2.00

%description
Log::Log4perl lets you remote-control and fine-tune the logging behaviour of
your system from the outside. It implements the widely popular (Java-based)
Log4j logging package in pure Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find lib -type f -exec chmod 644 {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
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

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1mdv2011.0
+ Revision: 684771
- update to new version 1.33

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.320.0-1
+ Revision: 643400
- update to new version 1.32

* Sun Jan 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.310.0-2mdv2011.0
+ Revision: 627622
- fix automatic dependencies: DBI and RRDs are only optionals
- spec cleanup

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.310.0-1mdv2011.0
+ Revision: 597074
- new version

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 575397
- update to 1.30

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.290.0-1mdv2011.0
+ Revision: 552411
- update to 1.29

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.1
+ Revision: 510978
- update to 1.28

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.1
+ Revision: 502103
- update to 1.27

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2010.1
+ Revision: 470457
- update to 1.26

* Tue Sep 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2010.0
+ Revision: 450852
- update to 1.25

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.0
+ Revision: 401637
- rebuild using %%perl_convert_version
- fixed license field

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2010.0
+ Revision: 394086
- update to new version 1.24

* Thu May 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1.23-1mdv2010.0
+ Revision: 375612
- update to new version 1.23

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.22-1mdv2010.0
+ Revision: 371560
- update to new version 1.22

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.21-1mdv2010.0
+ Revision: 369669
- update to new version 1.21

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 314250
- update to new version 1.20

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2009.1
+ Revision: 299391
- update to new version 1.19

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.0
+ Revision: 277952
- update to new version 1.18

* Mon Jul 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2009.0
+ Revision: 239315
- update to new version 1.17

* Wed May 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2009.0
+ Revision: 209688
- update to new version 1.16

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2008.1
+ Revision: 168826
- update to new version 1.15

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2008.1
+ Revision: 111152
- update to new version 1.14

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 1.13-1mdv2008.1
+ Revision: 100835
- update to new version 1.13

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2008.0
+ Revision: 47696
- update to new version 1.12

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.10-1mdv2008.0
+ Revision: 20262
- 1.10


* Sat Aug 19 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-19 13:10:56 (56887)
- 1.06

* Sat Aug 19 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-19 13:06:21 (56886)
Import perl-Log-Log4perl

* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2007.0
- New version 1.05

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdk
- New release 1.04

* Sun Mar 05 2006 Michael Scherer <misc@mandriva.org> 1.03-2mdk
- add Requires exception, to break dependencies loop, to fix bug #19365

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdk
- New release 1.03

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdk
- New release 1.02
- %%mkrel

* Tue Oct 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- New release 1.01
- drop requires exceptions
- don't ship tests in doc

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdk
- New release 1.00

* Tue Jan 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.51-1mdk
- 0.51
- Update BuildRequires
- Enable tests

* Sat Jul 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.47-1mdk
- 0.47

* Sat Jun 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.46-1mdk
- 0.46

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.45-1mdk
- 0.45

* Mon May 17 2004 Michael Scherer <misc@mandrake.org> 0.44-1mdk
- New release 0.44
- rpmbuildupdate aware

* Wed Jan 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.30-4mdk
- rebuild
- remove dependencies on perl(devel) modules



