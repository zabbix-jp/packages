# package for ZABBIX 1.4.7-1 Agent for Windows
# (C) 2005-2011 - ZABBIX-JP

# Content / Purpose
# -----------------
This package includes from 1.4.7-1 provided ZABBIX-JP
 - zabbix_agent for W32 & w64
 - zabbix_sender.exe
 - zabbix_get.exe
  

# Changelog
# -----------------
* Mon Feb 28 2011 Kazuo Ito <qyn02623@nifty.com> 1.4.7-1
- Update to 1.4.7
- Add a patch to improve slow query to show events screen (Patch15)
- Change /etc/zabbix/zabbix.conf.php permission
- Fix compile snmp localname error (patch17)

* Sun Sep 27 2009 Kodai Terashima <kodai74@gmail.com> 1.4.6-2
- Add a patch to allow multibyte trigger expression (Patch14)

* Fri Jul 3 2009 Kodai Terashima <kodai74@gmail.com> 1.4.6-1
- Update to 1.4.6
- Add a patch to fix copyright-year in locales file from MIRACLE LINUX (Patch6)
- Add a patch from MIRACLE LINUX to converter from SJIS to UTF-8 for Windows Event Log (Patch7)
- Add a patch from MIRACLE LINUX to support Japanese for Graph formula (Patch8)
- Add a patch from MIRACLE LINUX to fix does not switch Enable/Disable on items/web screen when use Japanese language (Patch9)
- Add a patch from MIRACLE LINUX to fix does not use color link on map when use Japanese language (Patch10)
- Add a patch from MIRACLE LINUX to fix exhausted memory by using DB cursor (Patch11)
- Add a patch from MIRACLE LINUX to allow item/trigger parameter to set multibyte character (Patch12)
- Add a patch to add link to ZABBIX-JP in footer (Patch13)
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
