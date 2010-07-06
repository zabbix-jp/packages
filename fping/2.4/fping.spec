Name: fping
Version: 2.4b2
Release: 16%{?dist}
Summary: Scriptable, parallelized ping-like utility
Group: Applications/Internet
License: BSD with advertising
URL: http://www.fping.com/
# upstream isn't really there any more
# Source0: http://www.fping.com/download/%{name}-%{version}_to-ipv6.tar.gz
Source0: %{name}-%{version}_to-ipv6.tar.gz
Patch0: fping-2.4b2_to-ipv6-16.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
fping is a ping-like program which can determine the accessibility of
multiple hosts using ICMP echo requests. fping is designed for parallelized
monitoring of large numbers of systems, and is developed with ease of
use in scripting in mind.

%prep
%setup -q -n %{name}-%{version}_to-ipv6
%patch0 -p1 -b .ipv6

%build
%configure
make CFLAGS="-DIPV6 $RPM_OPT_FLAGS"
mv fping fping6

make clean
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install
install -p -m 4755 fping6 "$RPM_BUILD_ROOT"/%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%attr(4755,root,root) %{_sbindir}/fping
%attr(4755,root,root) %{_sbindir}/fping6
%{_mandir}/man8/*

%changelog
* Sun Jul 4 2010 Kodai Terashima <kodai74@gmail.com> - 2.4b2-16
- Add S and T option from Debian patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 2.4b2-8
- Rebuild for GCC 4.3
- Fix license

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 2.4b2-7
- Bump and rebuild

* Tue Feb 14 2006 Chris Ricker <kaboom@oobleck.net> 2.4b2-6
- Bump and rebuild

* Wed Jun 29 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-5
- Clean up changelog and tags

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-4
- Bump release and build

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-3
- Add dist tag

* Mon May 16 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-3
- Simplify doc packaging (Matthias Saou)
- Simplify clean (Matthias Saou)
- Don't strip fping6 binary (Matthias Saou)
- Preserve timestamps

* Wed May 11 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-2
- Fix URL and Source locations

* Wed Mar 23 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-1
- Initial package for Fedora
- IPv6 patches from Herbert Xu (Debian)
