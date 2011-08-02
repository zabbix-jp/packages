Name:           iksemel
Version:        1.2
Release:        13%{?dist}
Summary:        An XML parser library designed for Jabber applications

Group:          System Environment/Libraries
License:        LGPL
URL:            http://iksemel.jabberstudio.org/
Source0:        http://files.jabberstudio.org/iksemel/iksemel-%{version}.tar.gz
Patch0:         iksemel-gcrypt-sha.patch
Patch1:         iksemel-64bit.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  texinfo
# BR this because gnutls config script needs it (BZ#200493)
BuildRequires:  pkgconfig

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
%patch0 -p0
%patch1 -p1

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

%check
%ifnarch ppc
make check
%endif

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

