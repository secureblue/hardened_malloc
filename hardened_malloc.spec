Name:           hardened_malloc
Version:        2025122500
Release:        1%{?dist}
Summary:        Hardened allocator designed for modern systems

License:        MIT
URL:            https://github.com/GrapheneOS/hardened_malloc
Source0:        opt.patch
BuildRequires:  systemd-rpm-macros rpm-build rpmdevtools make gcc gcc-c++ git-core
ExclusiveArch: x86_64 aarch64

%global debug_package %{nil}

# https://github.com/GrapheneOS/hardened_malloc/issues/200
# https://github.com/GrapheneOS/hardened_malloc/pull/253
%global optflags %{optflags} -fno-fat-lto-objects

%if 0%{?fedora} == 40
%undefine _ld_pack_relocs
%endif

%description
Hardened allocator designed for modern systems.

It has integration into Android's Bionic libc and can be used externally with
musl and glibc as a dynamic library for use on other Linux-based platforms. It
will gain more portability / integration over time.

# start section from https://github.com/divestedcg/rpm-hardened_malloc/blob/master/hardened_malloc.spec
#
# MIT License
#
# Copyright (c) 2022 noatsecure
# Copyright (c) 2022 Divested Computing Group
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

%prep

git clone --single-branch --branch=%{version} https://github.com/GrapheneOS/hardened_malloc.git

%define _srcdir hardened_malloc

%build

cd %{_srcdir};

cp config/default.mk config/pkey.mk
sed -i 's/CONFIG_SEAL_METADATA := false/CONFIG_SEAL_METADATA := true/' config/pkey.mk

patch -p1 < %{SOURCE0};


make CONFIG_NATIVE=false VARIANT=default;
make CONFIG_NATIVE=false VARIANT=light
make CONFIG_NATIVE=false VARIANT=pkey

%ifarch x86_64
ln -s default.mk config/default-x86-64.mk;
ln -s default.mk config/default-x86-64-v2.mk;
ln -s default.mk config/default-x86-64-v3.mk;
ln -s default.mk config/default-x86-64-v4.mk;

ln -s light.mk config/light-x86-64.mk;
ln -s light.mk config/light-x86-64-v2.mk;
ln -s light.mk config/light-x86-64-v3.mk;
ln -s light.mk config/light-x86-64-v4.mk;

ln -s pkey.mk config/pkey-x86-64.mk;
ln -s pkey.mk config/pkey-x86-64-v2.mk;
ln -s pkey.mk config/pkey-x86-64-v3.mk;
ln -s pkey.mk config/pkey-x86-64-v4.mk;

make CONFIG_NATIVE=false CONFIG_X86_64=true VARIANT=default-x86-64;
make CONFIG_NATIVE=false CONFIG_X86_64_V2=true VARIANT=default-x86-64-v2;
make CONFIG_NATIVE=false CONFIG_X86_64_V3=true VARIANT=default-x86-64-v3;
make CONFIG_NATIVE=false CONFIG_X86_64_V4=true VARIANT=default-x86-64-v4;

make CONFIG_NATIVE=false CONFIG_X86_64=true VARIANT=light-x86-64;
make CONFIG_NATIVE=false CONFIG_X86_64_V2=true VARIANT=light-x86-64-v2;
make CONFIG_NATIVE=false CONFIG_X86_64_V3=true VARIANT=light-x86-64-v3;
make CONFIG_NATIVE=false CONFIG_X86_64_V4=true VARIANT=light-x86-64-v4;

make CONFIG_NATIVE=false CONFIG_X86_64=true VARIANT=pkey-x86-64;
make CONFIG_NATIVE=false CONFIG_X86_64_V2=true VARIANT=pkey-x86-64-v2;
make CONFIG_NATIVE=false CONFIG_X86_64_V3=true VARIANT=pkey-x86-64-v3;
make CONFIG_NATIVE=false CONFIG_X86_64_V4=true VARIANT=pkey-x86-64-v4;
%endif

# end section from https://github.com/divestedcg/rpm-hardened_malloc/blob/master/hardened_malloc.spec

%install
install -Dm4644 -s %{_srcdir}/out/libhardened_malloc.so %{buildroot}%{_libdir}/libhardened_malloc.so
install -Dm4644 -s %{_srcdir}/out-light/libhardened_malloc-light.so %{buildroot}%{_libdir}/libhardened_malloc-light.so
install -Dm4644 -s %{_srcdir}/out-pkey/libhardened_malloc-pkey.so %{buildroot}%{_libdir}/libhardened_malloc-pkey.so


%ifarch x86_64
install -Dm4644 -s %{_srcdir}/out-default-x86-64/libhardened_malloc-default-x86-64.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64/libhardened_malloc.so
install -Dm4644 -s %{_srcdir}/out-default-x86-64-v2/libhardened_malloc-default-x86-64-v2.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v2/libhardened_malloc.so
install -Dm4644 -s %{_srcdir}/out-default-x86-64-v3/libhardened_malloc-default-x86-64-v3.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v3/libhardened_malloc.so
install -Dm4644 -s %{_srcdir}/out-default-x86-64-v4/libhardened_malloc-default-x86-64-v4.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v4/libhardened_malloc.so

install -Dm4644 -s %{_srcdir}/out-light-x86-64/libhardened_malloc-light-x86-64.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64/libhardened_malloc-light.so;
install -Dm4644 -s %{_srcdir}/out-light-x86-64-v2/libhardened_malloc-light-x86-64-v2.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v2/libhardened_malloc-light.so
install -Dm4644 -s %{_srcdir}/out-light-x86-64-v3/libhardened_malloc-light-x86-64-v3.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v3/libhardened_malloc-light.so
install -Dm4644 -s %{_srcdir}/out-light-x86-64-v4/libhardened_malloc-light-x86-64-v4.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v4/libhardened_malloc-light.so

install -Dm4644 -s %{_srcdir}/out-pkey-x86-64/libhardened_malloc-pkey-x86-64.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64/libhardened_malloc-pkey.so;
install -Dm4644 -s %{_srcdir}/out-pkey-x86-64-v2/libhardened_malloc-pkey-x86-64-v2.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v2/libhardened_malloc-pkey.so;
install -Dm4644 -s %{_srcdir}/out-pkey-x86-64-v3/libhardened_malloc-pkey-x86-64-v3.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v3/libhardened_malloc-pkey.so;
install -Dm4644 -s %{_srcdir}/out-pkey-x86-64-v4/libhardened_malloc-pkey-x86-64-v4.so %{buildroot}%{_libdir}/glibc-hwcaps/x86-64-v4/libhardened_malloc-pkey.so;
%endif

%check
cd %{_srcdir};
make test

%files
%license %{_srcdir}/LICENSE %{_srcdir}/CREDITS
%doc %{_srcdir}/README.md
%{_libdir}/libhardened_malloc.so
%{_libdir}/libhardened_malloc-light.so
%{_libdir}/libhardened_malloc-pkey.so
%ifarch x86_64
%{_libdir}/glibc-hwcaps/x86-64/libhardened_malloc.so
%{_libdir}/glibc-hwcaps/x86-64-v2/libhardened_malloc.so
%{_libdir}/glibc-hwcaps/x86-64-v3/libhardened_malloc.so
%{_libdir}/glibc-hwcaps/x86-64-v4/libhardened_malloc.so
%{_libdir}/glibc-hwcaps/x86-64/libhardened_malloc-light.so
%{_libdir}/glibc-hwcaps/x86-64-v2/libhardened_malloc-light.so
%{_libdir}/glibc-hwcaps/x86-64-v3/libhardened_malloc-light.so
%{_libdir}/glibc-hwcaps/x86-64-v4/libhardened_malloc-light.so
%{_libdir}/glibc-hwcaps/x86-64/libhardened_malloc-pkey.so
%{_libdir}/glibc-hwcaps/x86-64-v2/libhardened_malloc-pkey.so
%{_libdir}/glibc-hwcaps/x86-64-v3/libhardened_malloc-pkey.so
%{_libdir}/glibc-hwcaps/x86-64-v4/libhardened_malloc-pkey.so
%endif

%changelog
* Fri Jan 2 2026 N0L0L1N0L1F3 - 2025122500-1
- Use GrapheneOS release tags instead of branches

* Tue Dec 12 2023 rusty-snake - 12-5
- hardened_malloc.so: 4755 -> 4644

* Sun Dec 10 2023 rusty-snake - 12-4
- Set set-user-id bit on libhardened_malloc.so.
  Thanks to Tad for the finding and reporting.
  Fixes #2

* Sat Dec 09 2023 rusty-snake - 12-3
- Remove 30-hardened_malloc.conf, Fedora 39 does this by default

* Sat Dec 09 2023 rusty-snake - 12-2
- Add pkey variant

* Fri Sep 29 2023 rusty-snake - 12-1
- Update to version 12

* Sat Jan 22 2022 rusty-snake - 11-1
- Update to version 11

* Thu Jan 13 2022 rusty-snake - 10-1
- Update to version 10
- Add libhardened_malloc-light.so

* Mon Jan 3 2022 rusty-snake - 9-1
- Update to version 9

* Sun Nov 14 2021 rusty-snake - 8-3
- Install 30-hardened_malloc.conf under %%_sysctldir
- Cleanup the specfile

* Thu Sep 30 2021 rusty-snake - 8-2
- Disable the post-transaction scriptlet to insert hardened_malloc
  into `/etc/ld.so.preload

* Sat Sep 18 2021 rusty-snake - 8-1
- Initial hardened_malloc spec
