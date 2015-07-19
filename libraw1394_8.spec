%define oname	libraw1394
%define	major	8
%define	libname	%mklibname raw1394_ %{major}
%define	devname	%mklibname raw1394_ %{major} -d

Summary:	FireWire interface
Name:		%{oname}_%{major}
Version:	1.3.0
Release:	16
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.linux1394.org/
Source0:	http://www.linux1394.org/dl/%{oname}-%{version}.tar.gz
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
Conflicts:	%{oname}-utils

%description -n	%{name}-utils
This package contains a few utilities to send and receive raw data over
Firewire (ieee1394).

%if %{_lib} != "lib"
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

%package -n	%{devname}
Summary:	Development and include files for libraw1394
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This archive contains the header-files for libraw1394 development.

%prep
%setup -qn %{oname}-%{version}
#fix build with new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*
autoreconf -fi

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{name}-utils
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n %{libname}
%{_libdir}/libraw1394.so.%{major}*

%files -n %{devname}
%doc README NEWS AUTHORS
%{_includedir}/libraw1394
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/%{oname}.pc

