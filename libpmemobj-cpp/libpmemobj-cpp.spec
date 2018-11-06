%define min_libpmemobj_ver 1.4
%define upstreamversion 1.5

Name:		libpmemobj-cpp
Version:	1.5
Release:	1%{?dist}
Summary:	C++ bindings for libpmemobj
License:	BSD
URL:		http://pmem.io/pmdk/cpp_obj/

Source0:	https://github.com/pmem/%{name}/archive/%{upstreamversion}.tar.gz#/%{name}-%{upstreamversion}.tar.gz

BuildRequires:	libpmemobj-devel >= %{min_libpmemobj_ver}
BuildRequires:	cmake >= 3.3
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	pkgconfig
BuildRequires:	doxygen

# There's nothing x86-64 specific in this package, but we have
# to duplicate what spec for pmdk/libpmemobj has at the moment.
ExclusiveArch: x86_64

%description
This package contains header files for libpmemobj C++ bindings and C++
containers built on top of them.

# Specify a virtual Provide for libpmemobj++-static package, so the package
# usage can be tracked.
%package -n libpmemobj++-devel
Summary: C++ bindings for Persistent Memory Transactional Object Store library
Group: Development/Libraries
Provides: libpmemobj++-static = %{version}-%{release}
Requires: libpmemobj-devel >= %{min_libpmemobj_ver}

%description -n libpmemobj++-devel
This package contains header files for libpmemobj C++ bindings and C++
containers built on top of them.

The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming.

%files -n libpmemobj++-devel
%{_libdir}/pkgconfig/libpmemobj++.pc
%{_includedir}/libpmemobj++/*.hpp
%{_includedir}/libpmemobj++/detail/*.hpp
%{_includedir}/libpmemobj++/experimental/*.hpp
%{_docdir}/libpmemobj++-devel/*
%{_libdir}/libpmemobj++/cmake/libpmemobj++-config-version.cmake
%{_libdir}/libpmemobj++/cmake/libpmemobj++-config.cmake

%license LICENSE

%doc ChangeLog README.md

%global debug_package %{nil}

%prep
%setup -q

%build
mkdir build
cd build
%cmake .. -DCMAKE_INSTALL_DOCDIR=%{_docdir}/libpmemobj++-devel
%make_build

%install
cd build
%make_install

%check
cd build
ctest -V %{?_smp_mflags}

%changelog
* Tue Nov 6 2018 Marcin Ślusarz <marcin.slusarz@intel.com> - 1.5-1
- Initial RPM release
