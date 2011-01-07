Name:           zabbix
Version:        1.8.4
Release:        1%{?dist}
Summary:        Open-source monitoring solution for your IT infrastructure

Group:          Applications/Internet
License:        GPL
URL:            http://www.zabbix.com/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        zabbix-web.conf
Source2:        zabbix-server.init
Source3:        zabbix-agent.init
Source4:        zabbix-proxy.init
Source5:        zabbix-logrotate.in
Source6:        zabbix_agentd.conf
Source7:        zabbix_server.conf
Source8:        zabbix_proxy.conf
Source9:        ipagui.ttf
Source10:        enduser_license.txt
Source11:        zabbix-1.8.3-ja_jp.inc.php
#Source12:        eventlog.c
#Source13:       eventlog.h
Patch1:         zabbix-1.8-datasql.patch
Patch2:         zabbix-1.8.4-powered_by_zabbixjp.patch
#Patch3:         zabbix-1.8.2-fix_to_compile_visualstudio_proj.patch
Patch4:         zabbix-1.8.4-graph_font.patch
#Patch5:         zabbix-1.8-parentservice_translate.patch
#Patch6:         zabbix-1.8-chart4_use_imagetext.patch
#Patch7:         zabbix-1.8-loginmenu_translate.patch
#Patch8:         zabbix-1.8-wrong_usergroup_permission.patch
#Patch9:         zabbix-1.8-chart5_use_imagetext.patch
#Patch10:        zabbix-1.8-discoveryconf_seconds_translate.patch
Patch11:        zabbix-1.8-itservice_popup_translate.patch
#Patch12:        zabbix-1.8-installer_require_wrong_phpversion.patch
#Patch13:        zabbix-1.8-template_import.patch
#Patch14:        zabbix-1.8-popup_media_status_translate.patch
#Patch15:        zabbix-1.8-pie_chart.patch
#Patch16:         zabbix-1.8.2-setup_from_empty_conf.patch
Patch17:         zabbix-1.8.4-default_period.patch
Patch18:         zabbix-1.8.3-initial_datasql_status_and_error.patch

Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define is_el4 %(grep -i "release 4" /etc/redhat-release > /dev/null 2>&1 && echo 1 || echo 0)
%define is_el5 %(grep -i "release 5" /etc/redhat-release > /dev/null 2>&1 && echo 1 || echo 0) 

BuildRequires:   mysql-devel
BuildRequires:   postgresql-devel
BuildRequires:   net-snmp-devel
BuildRequires:   openldap-devel
BuildRequires:   gnutls-devel
BuildRequires:   iksemel-devel
BuildRequires:   sqlite-devel
BuildRequires:   unixODBC-devel
BuildRequires:   libssh2-devel >= 1.0.0

%if %is_el5
BuildRequires:   curl-devel >= 7.13.1
BuildRequires:   OpenIPMI-devel >= 2.0.14
%endif

Requires:        logrotate
Requires(pre):   /usr/sbin/useradd

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

%package server
Summary:         Zabbix server common files
Group:           Applications/Internet
Requires:        zabbix = %{version}-%{release}
Requires:        zabbix-server-implementation = %{version}-%{release}
Requires:        fping
Requires:        iksemel
Requires:        net-snmp
Requires:        unixODBC
Requires:        libssh2 >= 1.0.0
%if %is_el5
Requires:        curl >= 7.13.1
Requires:        OpenIPMI-libs >= 2.0.14
%endif
Conflicts:       zabbix-proxy
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description server
Zabbix server common files

%package server-mysql
Summary:         Zabbix server compiled to use MySQL
Group:           Applications/Internet
Requires:        zabbix = %{version}-%{release}
Requires:        zabbix-server = %{version}-%{release}
Requires:        mysql
Provides:        zabbix-server-implementation = %{version}-%{release}
Obsoletes:       zabbix <= 1.5.3-0.1
Conflicts:       zabbix-server-pgsql
Conflicts:       zabbix-server-sqlite3

%description server-mysql
Zabbix server compiled to use MySQL

%package server-pgsql
Summary:         Zabbix server compiled to use PostgresSQL
Group:           Applications/Internet
Requires:        zabbix = %{version}-%{release}
Requires:        zabbix-server = %{version}-%{release}
Requires:        postgresql
Provides:        zabbix-server-implementation = %{version}-%{release}
Conflicts:       zabbix-server-mysql
Conflicts:       zabbix-server-sqlite3

%description server-pgsql
Zabbix server compiled to use PostgresSQL

%package server-sqlite3
Summary:         Zabbix server compiled to use SQLite
Group:           Applications/Internet
Requires:        zabbix = %{version}-%{release}
Requires:        zabbix-server = %{version}-%{release}
Requires:        sqlite
Provides:        zabbix-server-implementation = %{version}-%{release}
Conflicts:       zabbix-server-mysql
Conflicts:       zabbix-server-pgsql

%description server-sqlite3
Zabbix server compiled to use SQLite

%package agent
Summary:         Zabbix Agent
Group:           Applications/Internet
Requires:        zabbix = %{version}-%{release}
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description agent
The Zabbix client agent, to be installed on monitored systems.

%package proxy
Summary:         Zabbix Proxy
Group:           Applications/Internet
Requires:        zabbix = %{version}-%{release}
Requires:        zabbix-proxy-implementation = %{version}-%{release}
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires:        fping
Requires:        net-snmp
Requires:        unixODBC
Requires:        libssh2 >= 1.0.0
%if %is_el5
Requires:        curl >= 7.13.1
Requires:        OpenIPMI-libs >= 2.0.14
%endif
Conflicts:       zabbix-web
Conflicts:       zabbix-server

%description proxy
The Zabbix proxy

%package proxy-mysql
Summary:         Zabbix proxy compiled to use MySQL
Group:           Applications/Internet
Requires:        zabbix-proxy = %{version}-%{release}
Requires:        mysql
Provides:        zabbix-proxy-implementation = %{version}-%{release}
Conflicts:       zabbix-proxy-pgsql
Conflicts:       zabbix-proxy-sqlite3

%description proxy-mysql
The Zabbix proxy compiled to use MySQL

%package proxy-pgsql
Summary:         Zabbix proxy compiled to use PostgreSQL
Group:           Applications/Internet
Requires:        zabbix-proxy = %{version}-%{release}
Requires:        postgresql
Provides:        zabbix-proxy-implementation = %{version}-%{release}
Conflicts:       zabbix-proxy-mysql
Conflicts:       zabbix-proxy-sqlite3

%description proxy-pgsql
The Zabbix proxy compiled to use PostgreSQL

%package proxy-sqlite3
Summary:         Zabbix proxy compiled to use SQLite
Group:           Applications/Internet
Requires:        zabbix-proxy = %{version}-%{release}
Requires:        sqlite
Provides:        zabbix-proxy-implementation = %{version}-%{release}
Conflicts:       zabbix-proxy-mysql
Conflicts:       zabbix-proxy-pgsql

%description proxy-sqlite3
The Zabbix proxy compiled to use SQLite

%package web
Summary:         Zabbix Web Frontend
Group:           Applications/Internet
Requires:        httpd
Requires:        php >= 5.0
Requires:        php-gd
Requires:        php-mbstring
Requires:        php-xml
Requires:        zabbix = %{version}-%{release}
Requires:        zabbix-web-database = %{version}-%{release}
%if %is_el5
Requires:        php-bcmath
%endif
Conflicts:       zabbix-proxy

%description web
The php frontend to display the zabbix web interface.

%package web-mysql
Summary:         Zabbix web frontend for MySQL
Group:           Applications/Internet
Requires:        zabbix-web = %{version}-%{release}
Requires:        php-mysql
Provides:        zabbix-web-database = %{version}-%{release}
Obsoletes:       zabbix-web <= 1.5.3-0.1
Conflicts:       zabbix-web-pgsql
Conflicts:       zabbix-web-sqlite3

%description web-mysql
Zabbix web frontend for MySQL

%package web-pgsql
Summary:         Zabbix web frontend for PostgreSQL
Group:           Applications/Internet
Requires:        zabbix-web = %{version}-%{release}
Requires:        php-pgsql
Provides:        zabbix-web-database = %{version}-%{release}
Conflicts:       zabbix-web-mysql
Conflicts:       zabbix-web-sqlite3

%description web-pgsql
Zabbix web frontend for PostgreSQL

%package web-sqlite3
Summary:         Zabbix web frontend for SQLite
Group:           Applications/Internet
Requires:        zabbix-web = %{version}-%{release}
Requires:        sqlite
Provides:        zabbix-web-database = %{version}-%{release}
Conflicts:       zabbix-web-mysql
Conflicts:       zabbix-web-pgsql

%description web-sqlite3
Zabbix web frontend for SQLite

%prep
%setup0 -q
%patch1 -p1 -b .datasql.orig
%patch2 -p1 -b .powered_by_zabbixjp.orig
#%patch3 -p1 -b .fix_to_compile_visualstudio_proj.orig
%patch4 -p1 -b .graph_font.orig
#%patch5 -p1 -b .parentservice_translate.orig
#%patch6 -p1 -b .chart4_use_imagestring.orig
#%patch7 -p1 -b .loginmenu_translate.orig
#%patch8 -p1 -b .wrong_usergroup_permission.orig
#%patch9 -p1 -b .chart5_use_imagetext.orig
#%patch10 -p1 -b .discoveryconf_seconds_translate.orig
%patch11 -p1 -b .itservice_popup_translate.orig
#%patch12 -p1 -b .installer_require_wrong_phpversion.orig
#%patch13 -p1 -b .template_import.orig
#%patch14 -p1 -b .popup_media_status_translate.orig
#%patch15 -p1 -b .pie_chart.orig
#%patch16 -p1 -b .setup_from_empty_conf.orig
%patch17 -p1 -b .default_period.orig
%patch18 -p1 -b .initial_datasql_status_and_error.orig

rm frontends/php/fonts/DejaVuSans.ttf
cp %{SOURCE9} %{SOURCE10} frontends/php/fonts/
rm frontends/php/include/locales/ja_jp.inc.php
cp %{SOURCE11} frontends/php/include/locales/ja_jp.inc.php
#cp %{SOURCE12} %{SOURCE13} src/zabbix_agent/

chmod -R a+rX .

# fix up some lib64 issues
%{__perl} -pi.orig -e 's|_LIBDIR=/usr/lib|_LIBDIR=%{_libdir}|g' \
    configure

%build

common_flags="
    --enable-server \
    --enable-agent \
    --enable-proxy \
    --enable-ipv6 \
    --with-net-snmp \
    --with-ldap \
    --with-unixodbc \
    --with-ssh2 \
  %if %is_el4
    --without-libcurl \
    --without-openipmi \
  %endif
  %if %is_el5
    --with-openipmi \
    --with-libcurl \
  %endif
    --with-jabber
"

%configure $common_flags --with-mysql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_mysql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_mysql

%configure $common_flags --with-pgsql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_pgsql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_pgsql

%configure $common_flags --with-sqlite3
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_sqlite3
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_sqlite3

touch src/zabbix_server/zabbix_server
touch src/zabbix_proxy/zabbix_proxy

%install
rm -rf $RPM_BUILD_ROOT
# set up some required directories
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/alertscripts
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/externalscripts
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix_agentd.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}

# php frontend
find ./frontends/php -name '*.orig'|xargs rm -f
find ./create -name '*.orig'|xargs rm -f
cp -a frontends/php $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/include/defines.inc.php \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
ln -s ../../../..%{_sysconfdir}/%{name}/defines.inc.php \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/include/defines.inc.php
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/maintenance.inc.php \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
ln -s ../../../..%{_sysconfdir}/%{name}/maintenance.inc.php \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/maintenance.inc.php
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix.conf.php
ln -s ../../../..%{_sysconfdir}/%{name}/zabbix.conf.php \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/zabbix.conf.php
# kill off .htaccess files, options set in SOURCE1
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/include/.htaccess
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/include/classes/.htaccess
# drop config files in place
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/zabbix.conf
install -m 0644 -p misc/conf/zabbix_agent.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 0644 -p %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix_agentd.conf
install -m 0644 -p %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix_server.conf
install -m 0644 -p %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/zabbix_proxy.conf
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf
# log rotation
cat %{SOURCE5} | sed -e 's|COMPONENT|server|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
cat %{SOURCE5} | sed -e 's|COMPONENT|agentd|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
cat %{SOURCE5} | sed -e 's|COMPONENT|proxy|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy
# init scripts
install -m 0755 -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-server
install -m 0755 -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-agent
install -m 0755 -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-proxy

# set up config dir

# install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_server
install -m 0755 -p src/zabbix_server/zabbix_server_* $RPM_BUILD_ROOT%{_sbindir}/
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy
install -m 0755 -p src/zabbix_proxy/zabbix_proxy_* $RPM_BUILD_ROOT%{_sbindir}/

# nuke static libs and empty oracle upgrade sql
rm -rf $RPM_BUILD_ROOT%{_libdir}/libzbx*.a
# nuke extraneous sql files
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/create

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# Add the "zabbix" user
/usr/sbin/useradd -c "Zabbix Monitoring System" \
        -s /sbin/nologin -r -d %{_localstatedir}/lib/%{name} zabbix 2> /dev/null || :

%post server
/sbin/chkconfig --add zabbix-server || :

%post server-mysql
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sbindir}/zabbix_server ]; then
     cd %{_sbindir}
     ln -s zabbix_server_mysql zabbix_server || :
  fi
fi

%post server-pgsql
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sbindir}/zabbix_server ]; then
    cd %{_sbindir}
    ln -s zabbix_server_pgsql zabbix_server || :
  fi
fi

%post server-sqlite3
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sbindir}/zabbix_server ]; then
    cd %{_sbindir}
    ln -s zabbix_server_sqlite3 zabbix_server || :
  fi
fi

%post agent
/sbin/chkconfig --add zabbix-agent || :

%post proxy
/sbin/chkconfig --add zabbix-proxy || :

%post proxy-mysql
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sbindir}/zabbix_proxy ]; then
    cd %{_sbindir}
    ln -s zabbix_proxy_mysql zabbix_proxy || :
  fi
fi

%post proxy-pgsql
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sbindir}/zabbix_proxy ]; then
    cd %{_sbindir}
    ln -s zabbix_proxy_pgsql zabbix_proxy || :
  fi
fi

%post proxy-sqlite3
if [ $1 -eq 1 ]; then
  if [ ! -f %{_sbindir}/zabbix_proxy ]; then
    cd %{_sbindir}
    ln -s zabbix_proxy_sqlite3 zabbix_proxy || :
  fi
fi

%preun server
if [ $1 -eq 0 ]
then
  /sbin/service zabbix-server stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del zabbix-server
fi

%preun server-mysql
if [ $1 -eq 0 ]; then
  if [ -L %{_sbindir}/zabbix_server ]; then
    rm -f %{_sbindir}/zabbix_server || :
  fi
fi

%preun server-pgsql
if [ $1 -eq 0 ]; then
  if [ -L %{_sbindir}/zabbix_server ]; then
    rm -f %{_sbindir}/zabbix_server || :
  fi
fi

%preun server-sqlite3
if [ $1 -eq 0 ]; then
  if [ -L %{_sbindir}/zabbix_server ]; then
    rm -f %{_sbindir}/zabbix_server || :
  fi
fi

%preun agent
if [ $1 -eq 0 ]
then
  /sbin/service zabbix-agent stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del zabbix-agent
fi

%preun proxy
if [ $1 -eq 0 ]
then
  /sbin/service zabbix-proxy stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del zabbix-proxy
fi

%preun proxy-mysql 
if [ $1 -eq 0 ]; then
  if [ -L %{_sbindir}/zabbix_proxy ]; then
    rm -f %{_sbindir}/zabbix_proxy || :
  fi
fi

%preun proxy-pgsql
if [ $1 -eq 0 ]; then
  if [ -L %{_sbindir}/zabbix_proxy ]; then
    rm -f %{_sbindir}/zabbix_proxy || :
  fi
fi

%preun proxy-sqlite3
if [ $1 -eq 0 ]; then
  if [ -L %{_sbindir}/zabbix_proxy ]; then
    rm -f %{_sbindir}/zabbix_proxy || :
  fi
fi

%postun server
if [ $1 -gt 1 ]; then
  /sbin/service zabbix-server condrestart >/dev/null 2>&1 || :
fi

%postun agent
if [ $1 -gt 1 ]; then
  /sbin/service zabbix-agent condrestart >/dev/null 2>&1 || :
fi

%postun proxy
if [ $1 -gt 1 ]; then
  /sbin/service zabbix-proxy condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix

%files server
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc upgrades/dbpatches create/data create/schema
%{_mandir}/man8/zabbix_server.8.*
%config(noreplace) %attr(600,zabbix,zabbix) %{_sysconfdir}/zabbix/zabbix_server.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%dir %{_sysconfdir}/zabbix/alertscripts
%dir %{_sysconfdir}/zabbix/externalscripts
%{_sysconfdir}/init.d/zabbix-server

%files server-mysql
%doc AUTHORS ChangeLog COPYING NEWS README
%defattr(-,root,root,-)
%{_sbindir}/zabbix_server_mysql

%files server-pgsql
%doc AUTHORS ChangeLog COPYING NEWS README
%defattr(-,root,root,-)
%{_sbindir}/zabbix_server_pgsql

%files server-sqlite3
%doc AUTHORS ChangeLog COPYING NEWS README
%defattr(-,root,root,-)
%{_sbindir}/zabbix_server_sqlite3

%files agent
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man8/zabbix_agentd.8.*
%{_mandir}/man1/zabbix_get.1.*
%{_mandir}/man1/zabbix_sender.1.*
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agent.conf
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%dir %{_sysconfdir}/zabbix/zabbix_agentd.d
%{_sysconfdir}/init.d/zabbix-agent
%{_sbindir}/zabbix_agent
%{_sbindir}/zabbix_agentd
%{_bindir}/zabbix_sender
%{_bindir}/zabbix_get

%files proxy
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc upgrades/dbpatches create/data create/schema
%{_mandir}/man8/zabbix_proxy.8.*
%config(noreplace) %attr(600,zabbix,zabbix) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%{_sysconfdir}/init.d/zabbix-proxy

%files proxy-mysql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sbindir}/zabbix_proxy_mysql

%files proxy-pgsql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sbindir}/zabbix_proxy_pgsql

%files proxy-sqlite3
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sbindir}/zabbix_proxy_sqlite3

%files web
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %attr(600,apache,apache) %{_sysconfdir}/zabbix/zabbix.conf.php
%config(noreplace) %{_sysconfdir}/zabbix/defines.inc.php
%config(noreplace) %{_sysconfdir}/zabbix/maintenance.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/zabbix.conf
%{_datadir}/zabbix

%files web-mysql
%defattr(-,root,root,-)

%files web-pgsql
%defattr(-,root,root,-)

%files web-sqlite3
%defattr(-,root,root,-)

%changelog
* Fri Jan 7 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.4-1
- Update to 1.8.4
- Add access control to api and config directory for web interface (Source1)
- Update config files (Source6, Source7, Source8)
- Change log file rotation by logroate, not zabbix (Source7, Source8)
- Update Japanese translation (Source11)
- Delete unnecessary patch (Patch 16)
- Add initial sql files for zabbix-proxy

* Thu Aug 26 2010 Kodai Terashima <kodai74@gmail.com> - 1.8.3-1
- Update to 1.8.3
- Delete patch fix_to_compile_visualstudio_proj.patch (Patch3)
- Update config files (Source6, Source7, Source8)
- Add require net-snmp package instead of net-snmp-libs for server and proxy
- Change default time period from 23:59 to 24:00 (Patch17)
- Fix wrong status and remove error message from templates in data.sql

* Fri May 21 2010 Kodai Terashima <kodai74@gmail.com> - 1.8.2-1
- Update to 1.8.2
- Change mbstring.func_overload to 6 in zabbix-web.conf
- Add parch to redirect web installer if db parameter is empty in zabbix.conf.php (Patch16)
- Update Japanese translation (Source11)
- Update parch for windows VisualStudio project file (Patch3)
- Update zabbix_server.conf and zabbix_agentd.conf to merge 1.8.2 default config file (Source6, Source7)
- Add upload_max_filesize and max_input_time in zabbix-web.conf (Source1)
- Delete eventlog.c and eventlog.h (Source12, Source13)
- Create symlink for zabbix_server_* and zabbix_proxy_* if first install
- Add using binary filename "zabbix_server" and "zabbix_proxy" in init scripts
- Add require version for libssh, curl, OpenIPMI, php
- Add conflict proxy and web packages
- Add --without-libcurl and --without-openipmi compile options for CentOS4
- Some improvements for spec file
- Add require net-snmp-libs, unixODBC, libssh2, curl, OpenIPMI-libs for proxy package
- Add require libssh2 for server package
- Add conflicts zabbix-proxy on zabbix-server/zabbix-web

* Mon Feb 2 2010 Kodai Terashima <kodai74@gmail.com> -1.8.1-1
- Update to 1.8.1
- Update Japanese translation for zabbix 1.8.1
- Update zabbix_agentd.conf, zabbix_server.conf, zabbix_proxy.conf

* Sun Jan 17 2010 Kodai Terashima <kodai74@gmail.com> - 1.8
- Update to 1.8
- Add patch to change default language to Japanese (Patch1)
- Add patch to add link to ZABBIX-JP in header and footer (Patch2)
- Add patch to fix compile windows agent (Patch3)
- Add patch to use Japanese font in graph (Patch4)
- Add patch to translate "Parent service" in IT Service screen (patch5)
- Add patch to use imageText function in chart4.php (Patch6)
- Add patch to translate login menu (Patch7)
- Add patch to wrong usergroup permission (Patch8)
- Add patch to use imageText function in chart5.php (Patch9)
- Add patch to translate "seconds" in discovery configuration screen (Patch10)
- Add patch to translate popup menu in IT Service screen (Patch11)
- Add patch to fix installer require wrong php version (Patch12)
- Add patch to fix import template (Patch13)
- Add patch to translate user media popup screen (Patch14)
- Add patch to fix pie chart (Patch15)

* Wed Dec 10 2009 Kodai Terashima <kodai74@gmail.com> - 1.7.4-1
- Update to 1.7.4
- Delete zabbix-1.7-checks_db_few_argument.patch

* Wed Dec 10 2009 Kodai Terashima <kodai74@gmail.com> - 1.7.3-1
- Update to 1.7.3
- Replace manual pdf file by README 

* Mon Nov 11 2009 Kodai Terashima <kodai74@gmail.com> - 1.7.2-1
- Update to 1.7.2
- Add libssh compile option

* Wed Nov 4 2009 Kodai Terashima <kodai74@gmail.com> -1.7.1-1
- Update to 1.7.1

* Tue Nov 3 2009 Kodai Terashima <kodai74@gmail.com> - 1.7-1
- Update to 1.7
- add patch checks_db_few_argument.patch

* Tue Oct 27 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.6-1
- Updat zabbix-1.6.6-locale-cn_zh.patch (Patch1)
- Delete zabbix-1.6.4-pdb_parse_counter_path.patch (Patch9)
- Delete zabbix-1.6.4-display_events.patch (Patch15)

* Tue Oct 27 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.5-1
- Update zabbix-1.6.5-copyright_year.patch (Patch3)
- Update zabbix-1.6.5-graph_description.patch (Patch4)
- Update zabbix-1.6.5-powered_by_zabbixjp.patch (Patch13)
- Delete zabbix-1.6.4-localized_colors.patch (Patch5)

* Sun Oct 18 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.4-1
- initialized package for ZABBIX-JP
- Update Japanese translation (Source6)
- fix the bug that cannot choose Japanese language (Patch1)
- Add a patch to support Japanese font for Graph and Map (Patch2,Patch4)
- Add a patch to fix copyright-year in locales file from MIRACLE LINUX (Patch3)
- Add a patch from MIRACLE LINUX to fix does not use color link on map when use Japanese language (Patch5)
- allow item/trigger parameter to set multibyte character from MIRACLE LINUX (Patch6)
- Add a patch to convert from SJIS to UTF-8 for Windows Event Log from MIRACLE LINUX(Patch7)
- Add a patch for fix crash windows 2000 agent from MIRACLE LINUX(Patch8,9)
- add system.swap.in and system.swap.out patch for LVM devices and other device-mapper devices from MIRACLE LINUX(Patch10)
- fix FormatMessage crash in case of aInsertStrs having more than 64 elements from MIRACLE LINUX(Patch11)
- Change data.sql to select Japanese locale by default (Patch12)
- Add link to ZABBIX-JP in header and footer (Patch13)
- Add a patch to allow multibyte trigger expression (Patch14)
- Add a patch to improve slow query to show events screen (Patch15)
- Add a patch to fix sum parameter on proc_info item (Patch16)
- Add a patch to fix LDAP library probrem when complie on Windows (Patch17)
- Add a patch to fix broken character probrem when compile on Windows (Patch18)

* Fri Jan 23 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-2
- Rebuild for MySQL 5.1.X

* Fri Jan 16 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-1
- Update to 1.6.2: http://www.zabbix.com/rn1.6.2.php

* Thu Dec  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-1
- Fix BZ#474593 by adding a requires.

* Wed Nov  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-1
- Update to 1.6.1

* Tue Sep 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6-1.1
- Bump release because forgot to add some new files.

* Thu Sep 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6-1
- Update to final 1.6

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.4.6-2
- Fix license tag.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-1
- Update to 1.4.6

* Mon Jul 07 2008 Dan Horak <dan[at]danny.cz> - 1.4.5-4
- add LSB headers into init scripts
- disable internal log rotation

* Fri May 02 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.5-3
- Seems the zabbix folks replaced the original 1.4.5 tarball with
  an updated tarball or something -- it actually does contain a
  tiny bit of additional code... So update to newer 1.4.5.

* Tue Apr 08 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.5-2
- Fix building w/postgresql (#441456)

* Tue Mar 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-1
- Update to 1.4.5

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.4-2
- Bump and rebuild with gcc 4.3

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
