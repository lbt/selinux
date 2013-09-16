#
# spec file for package libselinux
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libsepol_ver 2.1.9

Name:           libselinux
Version: 2.1.13_20130423
Release: 1
Url:            http://userspace.selinuxproject.org/
Summary:        SELinux library and simple utilities
License:        GPL-2.0 and SUSE-Public-Domain
Group:          System/Libraries

Source:         selinux-%{version}.tar.gz
#Source1:        selinux-ready
#Source2:        baselibs.conf
Patch0:         %{name}-rhat.patch
Patch1:         %{name}-ruby.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libsepol-devel >= %{libsepol_ver}
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig

%description
Security-enhanced Linux is a feature of the Linux(R) kernel and a
number of utilities with enhanced security functionality designed to
add mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds of
mandatory access control policies, including those based on the
concepts of Type Enforcement(R), Role-based Access Control, and
Multi-level Security.

libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.  Required for any applications that use the SELinux API.



%package -n libselinux1
Summary:        SELinux library and simple utilities
Group:          System/Libraries

%description -n libselinux1
Security-enhanced Linux is a feature of the Linux(R) kernel and a
number of utilities with enhanced security functionality designed to
add mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds of
mandatory access control policies, including those based on the
concepts of Type Enforcement(R), Role-based Access Control, and
Multi-level Security.

libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.  Required for any applications that use the SELinux API.



%package -n selinux-tools
Summary:        SELinux library and simple utilities
Group:          System/Base

%description -n selinux-tools
Security-enhanced Linux is a feature of the Linux(R) kernel and a
number of utilities with enhanced security functionality designed to
add mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds of
mandatory access control policies, including those based on the
concepts of Type Enforcement(R), Role-based Access Control, and
Multi-level Security.

libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.  Required for any applications that use the SELinux API.



%package devel
Summary:        Development Include Files and Libraries for SELinux
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libselinux1 = %{version}
#Automatic dependency on libsepol-devel via pkgconfig

%description devel
This package contains the development files, which are
necessary to develop your own software using libselinux.


%package devel-static
Summary:        Static development Include Files and Libraries for SELinux
Group:          Development/Libraries/C and C++
Requires:       libselinux-devel = %{version}

%description devel-static
This package contains the static development files, which are
necessary to develop your own software using libselinux.


%prep
%setup -q
%patch0 -p2
%patch1

%build
cd %{name}
make %{?_smp_mflags} LIBDIR="%{_libdir}" CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/%{_lib}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
cd %{name}
make DESTDIR="$RPM_BUILD_ROOT" LIBDIR="$RPM_BUILD_ROOT%{_libdir}" SHLIBDIR="$RPM_BUILD_ROOT/%{_lib}" BINDIR="$RPM_BUILD_ROOT%{_sbindir}" install
rm -f $RPM_BUILD_ROOT%{_sbindir}/compute_*
rm -f $RPM_BUILD_ROOT%{_sbindir}/deftype
rm -f $RPM_BUILD_ROOT%{_sbindir}/execcon
rm -f $RPM_BUILD_ROOT%{_sbindir}/getenforcemode
rm -f $RPM_BUILD_ROOT%{_sbindir}/getfilecon
rm -f $RPM_BUILD_ROOT%{_sbindir}/getpidcon
rm -f $RPM_BUILD_ROOT%{_sbindir}/mkdircon
rm -f $RPM_BUILD_ROOT%{_sbindir}/policyvers
rm -f $RPM_BUILD_ROOT%{_sbindir}/setfilecon
rm -f $RPM_BUILD_ROOT%{_sbindir}/selinuxconfig
rm -f $RPM_BUILD_ROOT%{_sbindir}/selinuxdisable
rm -f $RPM_BUILD_ROOT%{_sbindir}/getseuser
rm -f $RPM_BUILD_ROOT%{_sbindir}/selinux_check_securetty_context
mv $RPM_BUILD_ROOT%{_sbindir}/getdefaultcon $RPM_BUILD_ROOT%{_sbindir}/selinuxdefcon
mv $RPM_BUILD_ROOT%{_sbindir}/getconlist $RPM_BUILD_ROOT%{_sbindir}/selinuxconlist
#install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/selinux-ready

%post -n libselinux1 -p /sbin/ldconfig

%postun -n libselinux1 -p /sbin/ldconfig

%files -n selinux-tools
%defattr(-,root,root,-)
%{_sbindir}/avcstat
%{_sbindir}/getenforce
%{_sbindir}/getsebool
%{_sbindir}/matchpathcon
%{_sbindir}/selinuxconlist
%{_sbindir}/selinuxdefcon
%{_sbindir}/selinuxenabled
%{_sbindir}/setenforce
%{_sbindir}/togglesebool
#%%{_sbindir}/selinux-ready
%{_sbindir}/selinuxexeccon
%{_sbindir}/sefcontext_compile
%{_mandir}/man5/*
%{_mandir}/man8/*

%files -n libselinux1
%defattr(-,root,root,-)
/%{_lib}/libselinux.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libselinux.so
%dir %{_includedir}/selinux
%{_includedir}/selinux/*
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libselinux.pc

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libselinux.a

%changelog
