# package for ZABBIX 1.8.3-1 Agent for Windows
# (C) 2005-2010 - ZABBIX-JP

# Content / Purpose
# -----------------
This package includes from 1.8.3-1 provided ZABBIX-JP
 - zabbix_agent for W32 & w64
 - zabbix_sender.exe
 - zabbix_get.exe
  

# Changelog
# -----------------
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
