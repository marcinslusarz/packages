%define upstreamversion 1.5

Name:		pmdk-convert
Version:	1.5
Release:	1%{?dist}
Summary:	Conversion tool for PMDK pools
License:	BSD
URL:		https://github.com/pmem/pmdk-convert
Group:		System Environment/Base

Source0:	https://github.com/pmem/%{name}/archive/%{upstreamversion}.tar.gz#/%{name}-%{upstreamversion}.tar.gz
Source1:	https://github.com/pmem/pmdk/archive/1.0.tar.gz#/nvml-1.0.tar.gz
Source2:	https://github.com/pmem/pmdk/archive/1.1.tar.gz#/nvml-1.1.tar.gz
Source3:	https://github.com/pmem/pmdk/archive/1.2.3.tar.gz#/nvml-1.2.3.tar.gz
Source4:	https://github.com/pmem/pmdk/archive/1.3.1.tar.gz#/nvml-1.3.1.tar.gz
Source5:	https://github.com/pmem/pmdk/archive/1.4.2.tar.gz#/nvml-1.4.2.tar.gz
Source6:	https://github.com/pmem/pmdk/archive/1.5.tar.gz#/nvml-1.5.tar.gz

BuildRequires:	cmake >= 3.3
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	gdb

# PMDK is currently available only on x86_64
ExclusiveArch: x86_64

%description
pmdk-convert is a tool for conversion of PMDK pools from any version
to any consecutive version. Currently only libpmemobj pools require
conversion and this tool supports only those kind of pools.

%files
%{_bindir}/pmdk-convert
%{_mandir}/man1/pmdk-convert.1.gz
%{_libdir}/pmdk-convert/libpmem-convert.so
%{_libdir}/pmdk-convert/pmemobj_convert_v1.so
%{_libdir}/pmdk-convert/pmemobj_convert_v2.so
%{_libdir}/pmdk-convert/pmemobj_convert_v3.so
%{_libdir}/pmdk-convert/pmemobj_convert_v4.so
%{_libdir}/pmdk-convert/pmemobj_convert_v5.so

%license LICENSE

%doc ChangeLog README.md

%prep
%setup -q
cp %{S:1} .
cp %{S:2} .
cp %{S:3} .
cp %{S:4} .
cp %{S:5} .
cp %{S:6} .

%build
mkdir build
cd build
# TESTS_USE_FORCED_PMEM=ON to speed up tests on non-pmem file systems
%cmake .. -DTESTS_USE_FORCED_PMEM=ON
%make_build

%install
cd build
%make_install

%check
cd build
ctest -V

%if 0%{?__debug_package} == 0
%debug_package
%endif

%changelog
* Tue Nov 6 2018 Marcin Ślusarz <marcin.slusarz@intel.com> - 1.5-1
- Initial RPM release
