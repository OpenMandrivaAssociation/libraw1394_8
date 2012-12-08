%define	name	libraw1394_8
%define oname libraw1394
%define	version	1.3.0
%define release	%mkrel 8

%define	major		8
%define	libname		%mklibname raw1394_ %{major}
%define	develname	%mklibname raw1394_%major -d
%define staticname	%mklibname raw1394_%major -d -s

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://www.linux1394.org/dl/%{oname}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.linux1394.org/
Summary:	FireWire interface
Requires(post): coreutils

%description
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

The reason for making a library the interface to the kernel is to avoid
a program dependency on the kernel version, which would hinder development and
optimization of raw1394.  If development changed the protocol and made it
incompatible with previous versions only the libraw1394 has to be upgraded to
match the kernel version (instead of all applications).

%package -n	%{name}-utils
Group:		Communications
Summary:	Some small Firewire utilities
Conflicts: %oname-utils

%description -n	%{name}-utils
This package contains a few utilities to send and receive raw data over
Firewire (ieee1394).

%if %_lib != lib
%package -n	%{libname}
Group:		System/Libraries
Summary:	FireWire interface shared library

%description -n %{libname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

The reason for making a library the interface to the kernel is to avoid
a program dependency on the kernel version, which would hinder development and
optimization of raw1394.  If development changed the protocol and made it
incompatible with previous versions only the libraw1394 has to be upgraded to
match the kernel version (instead of all applications).

This package contains the shared library to run applications linked
with %{name}.
%endif

%package -n	%{develname}
Summary:	Development and include files for libraw1394
Summary(pt_BR):	Arquivos de desenvolvimento e cabe?alhos para o libraw1394
Summary(es):	Development and include files for libraw1394
Group:		Development/C
Group(pt_BR):	Desenvolvimento
Group(es):	Desarrollo
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This archive contains the header-files for libraw1394 development.

%package -n	%{staticname}
Summary:	Development components for libraw1394
Summary(pt_BR):	Componentes est?ticos de desenvolvimento para o libraw1394
Summary(es):	Development components for libraw1394
Group:		Development/C
Group(pt_BR):	Desenvolvimento
Group(es):	Desarrollo
Requires:	%{develname} = %{version}-%{release}

%description -n	%{staticname}
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This archive contains the static libraries (.a) 


%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %name-utils
%defattr(-,root,root)
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man*/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libraw1394.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README NEWS AUTHORS
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/%{oname}.pc

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libraw1394.a


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-8mdv2011.0
+ Revision: 661520
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-7mdv2011.0
+ Revision: 602600
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-6mdv2010.1
+ Revision: 520898
- rebuilt for 2010.1

  + Götz Waschk <waschk@mandriva.org>
    - remove wrong conflict

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.0-5mdv2010.0
+ Revision: 425695
- rebuild

* Wed Jan 07 2009 Götz Waschk <waschk@mandriva.org> 1.3.0-4mdv2009.1
+ Revision: 326473
- add conflict to the devel package

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 1.3.0-3mdv2009.1
+ Revision: 325308
- readd libraw1394 1.3.0
- fork libraw1394 package

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 1.3.0
      release: 2mdv2009.2
      revision: 217191
      Copying 1.3.0-2mdv2009.0 to releases/ directory.

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill ldconfig require as requested by pixel

  + Funda Wang <fwang@mandriva.org>
    - rebuild
    - New version 1.3.0

  + Adam Williamson <awilliamson@mandriva.org>
    - correct license to LGPLv2+
    - rebuild for 2008
    - no need to package COPYING and INSTALL
    - don't create /dev node manually (udev handles it)
    - correct license to LGPLv2.1
    - new devel policy
    - drop patch0 (merged upstream)
    - spec clean
    - switch to a proper version scheme (was previously using svn, but undeclared)
    - update to svn snapshot 172
    - Import libraw1394

