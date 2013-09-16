#
# spec file for package libsepol
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


Name:           libsepol
Version:        2.1.9
Release:        0
Url:            http://www.nsa.gov/selinux/
Summary:        SELinux binary policy manipulation library
License:        LGPL-2.1+
Group:          System/Libraries
Source:         selinux-%{version}.tar.gz
Source2:        baselibs.conf
#Patch:          libsepol-2.1.4-role_fix_callback.patch
#Patch2:         libsepol-rhat.patch
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

libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing policy
boolean settings.



%package -n libsepol1
Summary:        SELinux binary policy manipulation library
Group:          System/Libraries

%description -n libsepol1
Security-enhanced Linux is a feature of the Linux(R) kernel and a
number of utilities with enhanced security functionality designed to
add mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds of
mandatory access control policies, including those based on the
concepts of Type Enforcement(R), Role-based Access Control, and
Multi-level Security.

libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing policy
boolean settings.



%package devel
Summary:        Development Include Files and Libraries for SELinux policy manipulation
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libsepol1 = %{version}
Requires:       pkgconfig

%description devel
The libsepol-devel package contains the libraries and header
files needed for developing applications that manipulate binary
policies.



%package devel-static
Summary:        Development Include Files and Libraries for SELinux policy manipulation
Group:          Development/Libraries/C and C++
Requires:       libsepol-devel = %{version}

%description devel-static
The libsepol-devel-static package contains the static libraries
needed for developing applications that manipulate binary
policies.



%prep
# Adjusting %%setup since git-pkg unpacks to src/
# %%setup -q
%setup -q -n src
#%%patch -p1
#%%patch2 -p2

%build
cd %{name}
make %{?_smp_mflags} CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS)"

%install
mkdir -p $RPM_BUILD_ROOT/%{_lib}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{3,8}
cd %{name}
make DESTDIR="$RPM_BUILD_ROOT" LIBDIR="$RPM_BUILD_ROOT%{_libdir}" SHLIBDIR="$RPM_BUILD_ROOT/%{_lib}" install
rm -f $RPM_BUILD_ROOT%{_bindir}/genpolbools
rm -f $RPM_BUILD_ROOT%{_bindir}/genpolusers
rm -f $RPM_BUILD_ROOT%{_bindir}/chkcon
rm -rf $RPM_BUILD_ROOT%{_mandir}/man8

%post -n libsepol1 -p /sbin/ldconfig

%postun -n libsepol1 -p /sbin/ldconfig

%files -n libsepol1
%defattr(-,root,root)
/%{_lib}/libsepol.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libsepol.so
%{_mandir}/man3/*
%dir %{_includedir}/sepol
%{_includedir}/sepol/*.h
%dir %{_includedir}/sepol/policydb
%{_includedir}/sepol/policydb/*.h
%{_libdir}/pkgconfig/libsepol.pc

%files devel-static
%defattr(-,root,root)
%{_libdir}/libsepol.a

%changelog
