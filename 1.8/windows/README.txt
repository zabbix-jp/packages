# NSIS package for ZABBIX 1.8 Client for Windows
# (C) 2009 - Kodai Terashima <kodai74@gmail.com>

#          
# Content / Purpose
# -----------------
To build an EXE install package for ZABBIX Agent 1.8, using NSIS.
.\img\		: logs and pics
.\Include\	: nsh macros
.\Installer\	: ZABBIX components to install. Includes from ZABBIX 1.6.5 original zabbix_agentd.exe for win32 and win64 distribution,
		  zabbix_sender and zabbix_get precompiled exe.
ihm.ini		: custom page for zabbix_agentd.conf configuration
zabbix.nsi	: main NSIS script

How to use:
 . grab NSIS (rel 2.20 at least)
 . compile the zabbix.nsi with "makensis.exe"

Comments/Suggestions/Bugs reports => www.zabbix.com/forum

# How to use the resulting .exe install package for Windows
# ---------------------------------------------------------
To install Zabbix agent and sender, just run zabbix_agent-1.8-1.JP_installer.exe

To use silent install mode, use :
 zabbix_agent-1.8-1.JP_installer.exe [/server=ZabbixServerIPAddress] [/rmtcmd=1] [/S][/D=InstallPath]
 
where:
 . ZabbixServerIPAddress is the IP address of the ZABBIX server
 . rmtcmd: 1 to enable remote commands, 0 to disable remote command
 . /S: Silent mode. If not indicated on the command line, the install GUI will prompt
       for confirmation of the indicated parameters (server and rmtcmd).
 . /D=InstallPath :sets the default installation directory. It must be the last parameter used in the command line and must not contain any quotes, 
	even if the path contains spaces. 

 
 Note: If Zabbix agent was installed with the package zabbix_agent-1.1.x_installer.exe 
        the installation is uninstalled in silent mode and prompt for confiramtion in gui mode  

#Since the the installer 1.8.0.1  
#------------------------------
If you have multiple Zabbix server monitoring by network you can create a file in the installer directory calling it zabbixlist.csv like :

"NetworkAdress;ZabbixServeurAdress
 default;zabbix_server4
 192.168.1.0;zabbix_server1
 192.168.2.0;zabbix_server2
 192.168.3.0;zabbix_server1
 192.168.4.0;zabbix_server3"
			 

When the installer see this file it calculate the network adress and try to find it in the file and take the zabbix server attached to the network adress. 
If the network adress is not in the file it take the default line if there is otherwise he take the server adresse given in the parameters


You can add a directory name "script" in the installer directory : All file in this directory will be copy to the install path

Now the uninstaller wil only remove the basic files :
  Zabbix_agentd.pid, LICENSE.txt, README.txt, zabbix_agentd.conf, zabbix_agentd.exe, zabbix_get.exe, zabbix_sender.exe


# Credits
# -------
 . Vincent Besan - initial NSIS package for ZABBIX 1.1.2 - Win32
 . Diego Pedroso for his StrCase function
 . Chris Morgan for the getParameterValue function
 . NullSoft of course.
 . Kodai Terashima - Create Japanese package
 
# Links
# -----
 . http://nsis.sf.net/
 . http://www.nullsoft.com/
 . http://www.zabbix.com/
 . http://www.zabbix.jp
