Name:           libssh2
Version:        1.2.2
Release:        1%{?dist}
Summary:        A library implementing the SSH2 protocol

Group:          System Environment/Libraries
License:        BSD
URL:            http://www.libssh2.org/
Source0:        http://downloads.sourceforge.net/libssh2/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
BuildRequires:  zlib-devel   
BuildRequires:  pkgconfig

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        docs 
Summary:        Documentation for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    docs
The %{name}-docs package contains man pages and examples for
developing applications that use %{name}.


%prep
%setup -q

# make sure things are UTF-8...
for i in ChangeLog NEWS ; do
    iconv --from=ISO-8859-1 --to=UTF-8 $i > new
    mv new $i
done

%build
%configure --disable-static --enable-shared

make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} \; 

# clean things up a bit for packaging
( cd example && make clean )
rm -rf example/simple/.deps 
find example/ -type f '(' -name '*.am' -o -name '*.in' ')' -exec rm -v {} \;

%check
(cd tests && make check)

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/*.so.*

%files docs
%defattr(-,root,root,-)
%doc COPYING HACKING example/
%{_mandir}/man?/*

%files devel
%defattr(-,root,root,-)
%doc COPYING 
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig

%changelog
* Tue Jul 15 2008 David Juran <djuran@redhat.com> - 0.18-9
- Tagging sillyness

* Tue Jul  1 2008  <djuran@redhat.com> - 0.18-8
- Adapted for EPEL

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.18-7
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-6
- rebuild for new openssl...

* Tue Nov 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-5
- bump

* Tue Nov 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-4
- add INSTALL arg to make install vs env. var

* Mon Nov 26 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-3
- run tests; don't package test

* Sun Nov 18 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-2
- split docs into -docs (they seemed... large.)

* Tue Nov 13 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-1
- update to 0.18

* Sun Oct 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- update to 0.17
- many spec file changes

* Wed May 23 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.15-0.2.20070506
- Fix release tag
- Move manpages to -devel package
- Add Examples dir to -devel package

* Sun May 06 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.15-0.20070506.1
- Initial build
