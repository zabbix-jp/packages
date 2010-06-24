# package for ZABBIX 1.6.9-2 Agent for Windows
# (C) 2005-2010 - ZABBIX-JP

# Content / Purpose
# -----------------
This package includes from 1.6.9-2 provided ZABBIX-JP
 - zabbix_agent for W32 & w64
 - zabbix_sender.exe
 - zabbix_get.exe
  

# Changelog
# -----------------
* Thu Jun 24 2010 Kodai Terashima <kodai74@gmail.com> - 1.6.9-2
- Fix log is not collected when long log item key using multibyte string (Patch27)
- Fix enable/disable item action does not work in application screen (Patch28)
- Fix graph view when select over 372 day (Patch29)

* Thu May 6 2010 Kodai Terashima <kodai74@gmail.com> - 1.6.9-1
- Update 1.6.9
- Add mbstring.func_overload in zabbix-web.conf (Comentted out)
- Add BuildRequires unixODBC-devel for CentOS4
- Add BuildRequires OpenIPMI-devel for CentOS5
- Delete BuildRequires php-bcmath for CentOS4
- Add parch to redirect web installer if db parameter is empty in zabbix.conf.php
- Update windows agent installer script for win64

* Sun Mar 21 2010 Kodai Terashima <kodai74@gmail.com> - 1.6.8-2
- Fix label text is not in the right place on map (Patch4)
- Fix color selection frame is not appeared (Patch22)
- Fix color configuration is not upgraded correctly from 1.4 to 1.6  when use Japanese (Patch23)
- Fix map icon label is not used map default label location setting (Patch24)
- Fix counting string function in trigger (Patch25)

* Thu Dec 10 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.8-1
- Update to 1.6.8
- Update graph_description.patch to localize available chart and pie chart (Patch4)
- Merge frontend.patch into graph_description.patch (Patch2, Patch4)
- Add patch to fix show active check data on Latest Data screen (Patch20)
- Add patch to fix problem doesn't show screen (Patch21)
- enable with-openipmi option in configure script

* Sun Nov 22 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.7-1
- Update Japanese translation (Source6)
- Update zabbix-1.6.7-powered_by_zabbixjp.patch to use zabbix.com link except Japanese (Patch13)
- Translation "Parent Service" on IT Service (Patch19) 
- Delete zabbix-1.6.4-freeaddrinfo.patch (Patch8)
- Delete zabbix-1.6.4-eventlog_formatmessage_crash.patch (Patch11)
- Delete zabbix-1.6.4-proc_info_sum.patch (Patch16)

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
