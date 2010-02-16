# package for ZABBIX 1.6.8-3 Agent for Windows
# (C) 2000-2010   - MIRACLE LINUX CoORPEARION

# Content / Purpose
# -----------------
This package includes from 1.6.8-3 provided MIRACLE LINUX Corporation:
 - zabbix_agent for W32 & w64
 - zabbix_sender.exe
 - zabbix_get.exe
  

# Changelog
# -----------------

* Wed Jan 6 2010 Kodai Terashima <terashima@miraclelinux.com> 1.6.8-3%{?dist}
- Update graph_description.patch to localize available chart and pie chart (Patch9)
- Merge frontend.patch into graph_description.patch (Patch4, Patch9)
- Add patch to fix problem doesn't show screen (Patch29)
- Add patch to fix show active check data on Latest Data screen (Patch30)
- enable with-openipmi option in configure script
- Update Japanese translation (Source7)

* Mon Nov 16 2009 Takanori Suzuki <tsuzuki@miraclelinux.com> - 1.6.7-2%{?dist}
- Update to 1.6.7
- remove already included patches (Patch10,15,17)

* Fri Nov  6 2009 Takanori Suzuki <tsuzuki@miraclelinux.com> - 1.6.6-1%{?dist}
- Update to 1.6.6
- remove already included patches (Patch10,15,17)
- add logrotated file support (Patch23)
- fix processing of logs and eventlogs which become empty only on the agent side (Patch24)
- fix processing of proc_info[] function (Patch25)
- fix VisualStudio project file (Patch26)
- remove broken character which affects in compiling with VisualStudio (Patch27)
- fix package build environment and recompile packages to fix system.cpu.util function
- fix copyright-year in japanese (source7)
- remove sqlite build process from spec file

* Wed Sep 16 2009 Kodai Terashima <terashima@miraclelinux.com> - 1.6.4-6%{?dist}
- fix FormatMessage crash in case of aInsertStrs having more than 64 elements (Patch19)
- add a patch to select Japanese locale by default (Patch 20)
- add a patch to add "Powered by MIRACLE LINUX" on footer (Patch21)
- add a powered_by_miracle logo (Source6)
- add a ja_jp.inc.php and delete locale-ja_jp.patch (Source7, Patch15)
- add script for blocking update zabbix packages by axtu in zabbix.spec
- add php options for Japanese in zabbix-web.conf
- add a patch to allow multibyte trigger expression (Patch22)

* Fri Aug 28 2009 Takanori Suzuki <tsuzuki@miraclelinux.com> - 1.6.4-5%{?dist}
- add system.swap.in and system.swap.out patch for LVM devices and other device-mapper devices (Patch16,17)
- fix diff path in windows patch files to patch '-p1' option (Patch18)

* Mon Aug 17 2009 Kodai Terashima <terashima@miraclelinux.com> - 1.6.4-4%{?dist}
- Add a patch for fix crash windows 2000 agent (Patch16,17)

* Thu May 13 2009 Masayuki MORIYAMA <moriyama@miraclelinux.com> - 1.6.4-3%{?dist}
- Update Japanese translation (AXBug#6304, Patch15)
- modify zabbix-1.6.4-trigger_cond_multibyte_param.patch (AXBug#6306)

* Tue Apr  7 2009 Masayuki MORIYAMA <moriyama@miraclelinux.com> - 1.6.4-2%{?dist}
- merge Asianux modifications to the new package which based on 1.4.6-1.1%{?dist}
  - When updating zabbix, restart zabbix-server, zabbix-agent and zabbix-proxy
  - modify zabbix-web.conf not to be able to access zabbix-web page by default
    (AXBug#4525)
  - replace Source1
  - fix the bug that cannot choose Japanese language (Patch3, AXBug#4614)
  - modify date format for Chinese (Patch6) and Korean (Patch14) (AXBug#4801)
  - fix copyright-year in locales file(Patch7)
  - fix minor bugs related to CKJ locales(Patch9,10)
  - allow item/trigger parameter to set multibyte character(Patch11)
  - fix exhausted memory by using DB cursor(Patch12)
  - add converter from SJIS to UTF-8 for Windows Event Log(Patch13)
  - fix locale files to modify version by itself

* Mon Apr 6 2009 Yoshihiro Kagawa <ykagawa@miraclelinux.com> - 1.6.4-1
- Update to 1.6.4
