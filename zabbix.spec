%define is_el4 %(grep -i "release 4" /etc/redhat-release > /dev/null 2>&1 && echo 1 || echo 0)
%define is_el5 %(grep -i "release 5" /etc/redhat-release > /dev/null 2>&1 && echo 1 || echo 0) 

Name:           zabbix
Version:        1.4.6
Release:        1%{?dist}
Summary:        Open-source monitoring solution for your IT infrastructure

Group:          Applications/Internet
License:        GPL
URL:            http://www.zabbix.com/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        zabbix-web.conf
Source2:        zabbix-server.init
Source3:        zabbix-agent.init
Source4:        zabbix-logrotate.in
Source5:        zabbix-1.4.5-ja_jp.inc.php
Source6:        zabbix.conf.php
Patch0:         zabbix-1.4.2-cpustats.patch
Patch1:	        zabbix-1.4.4-lcrypto.patch
Patch2:         zabbix-1.4.5-locale.patch
Patch3:         zabbix-1.4.5-frontend.patch
Patch4:	        zabbix-1.4.5-datasql.patch
Patch5:         zabbix-1.4.5-loglength.patch
Patch6:         zabbix-1.4.6-copyright_year.patch
Patch7:         zabbix-1.4.6-eventlog_acp_to_utf8.patch
Patch8:         zabbix-1.4.6-graph_description.patch
Patch9:         zabbix-1.4.6-literal_selected.patch
Patch10:        zabbix-1.4.6-localized_colors.patch
Patch11:        zabbix-1.4.6-trevent_memory_exhaustedfix.patch
Patch12:        zabbix-1.4.6-trigger_cond_multibyte_param.patch
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%define database mysql
%define zdb mysql
%define with_postgresql %{?_with_postgresql: 1} %{?!_with_postgresql: 0}

# Zabbix can only be built with mysql -or- postgresql
# support. We build with mysql by default, but you can
# pass --with postgresql to build with postgresql instead.
%if %{with_postgresql}
%define database postgresql
%define zdb pgsql
%endif

BuildRequires:  %{database}-devel, net-snmp-devel
BuildRequires:  openldap-devel, gnutls-devel
%if %is_el4
BuildRequires:  iksemel-devel
%endif
%if %is_el5
BuildRequires:  iksemel-devel, curl-devel
%endif
Requires:       logrotate, fping, net-snmp-libs
Requires(pre):      /usr/sbin/useradd
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service

%description
ZABBIX is software that monitors numerous parameters of a
network and the health and integrity of servers. ZABBIX
uses a flexible notification mechanism that allows users
to configure e-mail based alerts for virtually any event.
This allows a fast reaction to server problems. ZABBIX
offers excellent reporting and data visualisation features
based on the stored data. This makes ZABBIX ideal for
capacity planning.

ZABBIX supports both polling and trapping. All ZABBIX
reports and statistics, as well as configuration
parameters are accessed through a web-based front end. A
web-based front end ensures that the status of your network
and the health of your servers can be assessed from any
location. Properly configured, ZABBIX can play an important
role in monitoring IT infrastructure. This is equally true
for small organisations with a few servers and for large
companies with a multitude of servers.


%package agent
Summary:        Zabbix Agent
Group:          Applications/Internet
Requires:       logrotate
Requires(pre):      /usr/sbin/useradd
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service

%description agent
The zabbix client agent, to be installed on monitored systems.

%package web
Summary:        Zabbix Web Frontend
Group:          Applications/Internet
%if %is_el4
Requires:       php, php-%{zdb}, php-gd, php-mbstring, ttfonts-ja
%endif
%if %is_el5
Requires:       php, php-%{zdb}, php-gd, php-bcmath, php-mbstring, fonts-japanese
%endif

%description web
The php frontend to display the zabbix web interface.

%prep
%setup -q

rm frontends/php/include/locales/ja_jp.inc.php
cp %{SOURCE5} frontends/php/include/locales/ja_jp.inc.php

%patch0 -p1 -b .cpustats.orig
%patch1 -p1 -b .lcrypto.orig
%patch2 -p1 -b .locale.orig
%patch3 -p1 -b .frontend.orig
%patch4 -p1 -b .datasql.orig
%patch5 -p1 -b .loglength.orig
%patch6 -p1 -b .copyright_year.orig
%patch7 -p1 -b .eventlog_acp_to_utf8.orig
%patch8 -p1 -b .graph_description.orig
%patch9 -p1 -b .literal_selected.orig
%patch10 -p1 -b .localized_colors.orig
%patch11 -p1 -b .trevent_memory_exhaustedfix.orig
%patch12 -p1 -b .trigger_cond_multibyte_param.orig

# shuffle sql init files around to fix up install
mkdir -p dbinit/{schema,data}
cp create/schema/%{database}.sql dbinit/schema/
cp create/data/images_%{database}.sql dbinit/data/
cp create/data/data.sql dbinit/data/

# fix up some lib64 issues
%{__perl} -pi.orig -e 's|_LIBDIR=/usr/lib|_LIBDIR=%{_libdir}|g' \
    configure

%build
%configure \
    --enable-server \
    --enable-agent \
    --with-%{zdb} \
    --with-net-snmp \
    --with-ldap \
    --with-jabber \
  %if %is_el5
    --with-libcurl
  %endif

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
# set up some required directories
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}
# php frontend
find ./frontends/php -name '*.orig'|xargs rm -f
cp -a frontends/php $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/include/db.inc.php \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
ln -s ../../../..%{_sysconfdir}/%{name}/db.inc.php \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/include/db.inc.php
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix.conf.php
ln -s ../../../..%{_sysconfdir}/%{name}/zabbix.conf.php \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/zabbix.conf.php
# kill off .htaccess files, options set in SOURCE1
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/include/.htaccess
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/include/classes/.htaccess
# drop config files in place
install -m 0644 misc/conf/zabbix_agent.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cat misc/conf/zabbix_agentd.conf | sed \
    -e 's|PidFile=.*|PidFile=%{_localstatedir}/run/zabbix/zabbix_agentd.pid|g' \
    -e 's|LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_agentd.log|g' \
    > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix_agentd.conf
cat misc/conf/zabbix_server.conf | sed \
    -e 's|PidFile=.*|PidFile=%{_localstatedir}/run/zabbix/zabbix.pid|g' \
    -e 's|LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_server.log|g' \
    -e 's|AlertScriptsPath=/home/zabbix/bin/|AlertScriptsPath=%{_localstatedir}/lib/zabbix/|g' \
    -e 's|DBUser=root|DBUser=zabbix|g' \
    -e 's|DBSocket=/tmp/mysql.sock|DBSocket=%{_localstatedir}/lib/%{zdb}/%{zdb}.sock|g' \
    > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix_server.conf
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf
# log rotation
cat %{SOURCE4} | sed -e 's|COMPONENT|server|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix
cat %{SOURCE4} | sed -e 's|COMPONENT|agentd|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
# init scripts
install -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix
install -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-agent

# set up config dir

# install
make DESTDIR=$RPM_BUILD_ROOT install

# nuke static libs and empty oracle upgrade sql
rm -rf $RPM_BUILD_ROOT%{_libdir}/libzbx*.a upgrades/dbpatches/1.4/oracle
# nuke extraneous sql files
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/create
# nuke erronious executable permissions
chmod -x src/zabbix_agent/eventlog.c


%clean
rm -rf $RPM_BUILD_ROOT

%pre
# Add the "zabbix" user
/usr/sbin/useradd -c "Zabbix Monitoring System" \
        -s /sbin/nologin -r -d %{_localstatedir}/lib/%{name} zabbix 2> /dev/null || :

%pre agent
# Add the "zabbix" user
/usr/sbin/useradd -c "Zabbix Monitoring System" \
        -s /sbin/nologin -r -d %{_localstatedir}/lib/%{name} zabbix 2> /dev/null || :

%post
/sbin/chkconfig --add zabbix

%post agent
/sbin/chkconfig --add zabbix-agent

%preun
if [ "$1" = 0 ]
then
  /sbin/service zabbix stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del zabbix
fi

%preun agent
if [ "$1" = 0 ]
then
  /sbin/service zabbix-agent stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del zabbix-agent
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING FAQ NEWS README
%doc docs/*.pdf upgrades/dbpatches dbinit
%dir %{_sysconfdir}/%{name}
%{_sbindir}/zabbix_server
%{_sysconfdir}/init.d/zabbix
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix
%config(noreplace) %{_sysconfdir}/%{name}/zabbix_server.conf
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/%{name}
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/%{name}

%files agent
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING FAQ NEWS README
%dir %{_sysconfdir}/%{name}
%{_sbindir}/zabbix_agent
%{_sbindir}/zabbix_agentd
%{_sbindir}/zabbix_sender
%{_sbindir}/zabbix_get
%{_sysconfdir}/init.d/zabbix-agent
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%config(noreplace) %{_sysconfdir}/%{name}/zabbix_agent.conf
%config(noreplace) %{_sysconfdir}/%{name}/zabbix_agentd.conf
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/%{name}
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/%{name}

%files web
%defattr(-,root,root,-)
%doc README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/zabbix.conf.php
%config(noreplace) %{_sysconfdir}/%{name}/db.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/audio
%dir %{_datadir}/%{name}/conf
%dir %{_datadir}/%{name}/images
%dir %{_datadir}/%{name}/include
%dir %{_datadir}/%{name}/js
%{_datadir}/%{name}/*.php
%{_datadir}/%{name}/css.css
%{_datadir}/%{name}/audio/*
%{_datadir}/%{name}/conf/*
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/include/*
%{_datadir}/%{name}/js/*

%changelog
* Fri Jul 3 2009 Kodai Terashima <kodai74@gmail.com> 1.4.6-1
- Update to 1.4.6
- Add a patch to fix copyright-year in locales file from MIRACLE LINUX (Patch6)
- Add a patch from MIRACLE LINUX to converter from SJIS to UTF-8 for Windows Event Log (Patch7)
- Add a patch from MIRACLE LINUX to support Japanese for Graph formula (Patch8)
- Add a patch from MIRACLE LINUX to fix does not switch Enable/Disable on items/web screen when use Japanese language (Patch9)
- Add a patch from MIRACLE LINUX to fix does not use color link on map when use Japanese language (Patch10)
- Add a patch from MIRACLE LINUX to fix exhausted memory by using DB cursor (Patch11)
- Add a patch from MIRACLE LINUX to allow item/trigger parameter to set multibyte character (Patch12)
- Merge el5.spec with el4.spec

* Wed Apr 15 2009 Kodai Terashima <kodai74@gmail.com> 1.4.5-2
- Add a patch to fix compilation on x86_64 architecture (Patch1)
- Add a patch to fix selecting Japanese language when selected Chinese language (Patch2)
- Add a patch to support Japanese font for Graph and Map (Patch3)
- Update Japanese locale (Source5)
- Change data.sql to select Japanese locale by default (Source6)
- Add PHP Configuration to zabbix.conf
- Add Requires: fonts-japanese to zabbix-web

* Wed Apr 02 2008 Kodai Terashima <kodai74@gmail.com> 1.4.5-1
- New upstream release

* Mon Dec 17 2007 Jarod Wilson <jwilson@redhat.com> - 1.4.4-1
- New upstream release
- Fixes two crasher bugs in 1.4.3 release

* Wed Dec 12 2007 Jarod Wilson <jwilson@redhat.com> - 1.4.3-1
- New upstream release

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.2-5
- Rebuild for deps

* Sat Dec 01 2007 Dan Horak <dan[at]danny.cz> 1.4.2-4
- add security fix (#407181)

* Thu Sep 20 2007 Dan Horak <dan[at]danny.cz> 1.4.2-3
- Add a patch to clean a warning during compile
- Add a patch to fix cpu load computations

* Tue Aug 21 2007 Jarod Wilson <jwilson@redhat.com> 1.4.2-2
- Account for binaries moving from %%_bindir to %%_sbindir

* Tue Aug 21 2007 Jarod Wilson <jwilson@redhat.com> 1.4.2-1
- New upstream release

* Mon Jul 02 2007 Jarod Wilson <jwilson@redhat.com> 1.4.1-1
- New upstream release

* Fri Jun 29 2007 Jarod Wilson <jwilson@redhat.com> 1.4-3
- Install correct sql init files (#244991)
- Add Requires: php-bcmath to zabbix-web (#245767)

* Wed May 30 2007 Jarod Wilson <jwilson@redhat.com> 1.4-2
- Add placeholder zabbix.conf.php

* Tue May 29 2007 Jarod Wilson <jwilson@redhat.com> 1.4-1
- New upstream release

* Fri Mar 30 2007 Jarod Wilson <jwilson@redhat.com> 1.1.7-1
- New upstream release

* Wed Feb 07 2007 Jarod Wilson <jwilson@redhat.com> 1.1.6-1
- New upstream release

* Thu Feb 01 2007 Jarod Wilson <jwilson@redhat.com> 1.1.5-1
- New upstream release

* Tue Jan 02 2007 Jarod Wilson <jwilson@redhat.com> 1.1.4-5
- Add explicit R:php to zabbix-web (#220676)

* Wed Dec 13 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-4
- Fix snmp polling buffer overflow (#218065)

* Wed Nov 29 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-3
- Rebuild for updated libnetsnmp

* Thu Nov 16 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-2
- Fix up pt_br
- Add Req-pre on useradd

* Wed Nov 15 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-1
- Update to 1.1.4

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-3
- Add BR: gnutls-devel, R: net-snmp-libs

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-2
- Fix php-pgsql Requires

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-1
- Update to 1.1.3

* Mon Oct 02 2006 Jarod Wilson <jwilson@redhat.com> 1.1.2-1
- Update to 1.1.2
- Enable alternate building with postgresql support

* Thu Aug 17 2006 Jarod Wilson <jwilson@redhat.com> 1.1.1-2
- Yank out Requires: mysql-server
- Add Requires: for php-gd and fping

* Tue Aug 15 2006 Jarod Wilson <jwilson@redhat.com> 1.1.1-1
- Update to 1.1.1
- More macroification
- Fix up zabbix-web Requires:
- Prep for enabling postgres support

* Thu Jul 27 2006 Jarod Wilson <jwilson@redhat.com> 1.1-2
- Add Requires: on chkconfig and service
- Remove openssl-devel from BR, mysql-devel pulls it in
- Alter scriptlets to match Fedora conventions

* Tue Jul 11 2006 Jarod Wilson <jwilson@redhat.com> 1.1-1
- Initial build for Fedora Extras
