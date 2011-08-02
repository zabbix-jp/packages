Name:           iksemel
Version:        1.4
Release:        2%{?dist}
Summary:        An XML parser library designed for Jabber applications

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://code.google.com/p/iksemel/
Source0:        http://iksemel.googlecode.com/files/iksemel-%{version}.tar.gz
Patch0:         0001-Fix-issues-compiling-with-newer-gnutls.patch
Patch1:         0002-Strip-out-internal-SHA-code-and-use-functions-from-g.patch
Patch2:         0003-Fix-alignment-on-architectures-where-doubles-are-64b.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  texinfo

%description
An XML parser library designed for Jabber applications. It is coded in
ANSI C for POSIX compatible environments, thus highly portable.

%package devel
Group:          Development/Libraries
Summary:        Development files for iksemel

Requires:       %{name} = %{version}-%{release}
Requires:       gnutls-devel
Requires:       pkgconfig

Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description devel
Development files for iksemel.

%package utils
Group:          Applications/Internet
Summary:        Development files for iksemel
Requires:       %{name} = %{version}-%{release}

%description utils
Utlity programs for iksemel.

%prep
%setup0 -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# force rebuilding of the info file
rm doc/iksemel

%build
# We need to re-run the autotools because the patch we apply modifies
# the configure.ac and src/Makefile.am
libtoolize --copy --force --automake
aclocal
autoheader
automake --add-missing --force-missing --gnu --include-deps
autoconf
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

mv %{buildroot}%{_infodir}/iksemel %{buildroot}%{_infodir}/iksemel.info
rm -f %{buildroot}%{_infodir}/dir

%check
make check

%clean
rm -rf %{buildroot}

%postun -p /sbin/ldconfig

%post -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun devel
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README TODO

%{_libdir}/libiksemel.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING

%{_libdir}/libiksemel.so
%{_includedir}/iksemel.h
%{_libdir}/pkgconfig/iksemel.pc
%{_infodir}/iksemel.info*

%files utils
%defattr(-,root,root,-)
%doc COPYING

%{_bindir}/ikslint
%{_bindir}/iksperf
%{_bindir}/iksroster

%changelog
* Wed Mar 24 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4-2
- Add patch from Quentin Armitage to fix alignment errors

* Thu Oct 22 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4-1
- Update to 1.4
- Apply patch from upstream so that gnutls autoconf works.
- Update gcrypt-sha patch so that it applies.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Dennis Gilmore <dennis@ausil.us> - 1.3-6
- disable "make check" on sparcv9

* Wed Jun 25 2008 Tomas Mraz <tmraz@redhat.com> - 1.3-5
- rebuild with new gnutls
- remove texinfo dir file from buildroot

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-4
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3-3
- Rebuild for GCC 4.3

* Sat Aug 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3-2
- Disable "make check" on PPC again.

* Sat Aug 25 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.3-1
- Update to 1.3
- Don't need to BR pkgconfig because gnutls-devel now requires it properly.
- Update license.
- Run "make check" on PPC
- Update patches so that they apply to 1.3
- Update URLs

* Thu Nov 16 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-13
- ppp != ppc

* Thu Nov 16 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-12
- Don't run make check on PPC - tests failing.

* Thu Nov 16 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-11
- Add patch from Hans de Goede that fixes 64 bit issues
- Re-enable "make check".
- Remove tabs from specfile.

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-10
- Bump release and rebuild.

* Wed Aug  2 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-6
- Temporarily disable make check until problems with it can be figured out.

* Thu Jul 27 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-5
- Patch to use SHA1 hashing routines from libgcrypt rather than
  broken internal code.  This means that we need to BR autoools
  to regenerate comfigure script and makefiles.

* Mon Jun 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-4
- Don't re-run autotools, fix rpath in a different way.

* Mon Jun 26 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-3
- Add a %check section.
- Add BR for libtool.

* Tue May 30 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-2
- Add texinfo BR

* Mon May 29 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.2-1
- First version for Fedora Extras.

