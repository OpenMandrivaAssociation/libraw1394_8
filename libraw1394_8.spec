%define	name	libraw1394_8
%define oname libraw1394
%define	version	1.3.0
%define release	%mkrel 6

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
%{_libdir}/libraw1394.la
%{_libdir}/pkgconfig/%{oname}.pc

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libraw1394.a
