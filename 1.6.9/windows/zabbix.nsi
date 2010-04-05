;  (C) 2006-2009 - Michel Manceron <michel.manceron@siemens.com>
;                - Vincent Besan輟n <elguapito@free.fr>
;                - Kodai Terashima <kodai74@gmail.com> (ZABBIX-JP)
; Quick & (not so) Dirty package for ZABBIX 1.6.8 client for Windows

;--------------------------------
;Includes
  !include "FileFunc.nsh"
  ; Modern UI
  !include "MUI.nsh"
  ; Text Functions
  !include ".\include\TextFunc.nsh"
  ; LogicLib
  !include ".\include\LogicLib.nsh"
  ; StrCase (see Include\StrCase.nsh for author info)
  !include ".\Include\StrCase.nsh"
  ;
  !include ".\include\GetParameters.nsh"
  !include ".\include\strstr.nsh"
  !include ".\include\GetParameterValue.nsh"
;--------------------------------
;General
!define NAME  "ZABBIX Agent"
!define VERSION "1.6.8"
!define VER_PACK "1.6.9.1"
!define DISPLAY_NAME "1.6.9-1.JP"
  ;Name and file
  Name "${NAME}"
  OutFile "zabbix_agent-${DISPLAY_NAME}_installer.exe"

  ;Default installation folder
  InstallDir "$PROGRAMFILES\${NAME}"
  
  ; Product Information
  VIAddVersionKey "ProductName" "${NAME}"
  VIAddVersionKey "CompanyName" "ZABBIX"
  VIAddVersionKey "LegalCopyright" "ZABBIX SIA & ZABBIX-JP"
  VIAddVersionKey "FileDescription" "${NAME} Installer 32 and 64 bits"
  VIAddVersionKey "FileVersion" "${VERSION}"

  VIProductVersion "${VER_PACK}"

; Registry key to check for directory (so if you install again, it will 
  ; overwrite the old one automatically)
  InstallDirRegKey HKLM "Software\${NAME}" "Install_Dir"
;--------------------------------
;Variables definitions

Var OUT
Var HOST
Var SERVER
Var RMTCMD
Var TMPHOST
Var OS64B
;--------------------------------
;Macros definitions
!macro PARAMETERNAME ParamName DefaultValue
  Push "${ParamName}" 
  Push "${DefaultValue}" 
  Call GetParameterValue
  Pop $${ParamName}
!macroend


!insertmacro ConfigWrite
!insertmacro un.DirState


;--------------------------------
;Interface Settings
  !define MUI_ICON ".\img\zabbix.ico"
  !define MUI_UNICON ".\img\zabbix.ico"
  !define MUI_HEADERIMAGE
  !define MUI_HEADERIMAGE_BITMAP ".\img\zabbix_logo.bmp"
  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE ".\Installer\docs\LICENSE.txt"
  !insertmacro MUI_PAGE_COMPONENTS
  ; Custom page to set some options in config file
  Page custom ConfigOptions
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "Japanese"

;--------------------------------
;Reserve Files
  
  ;These files should be inserted before other files in the data block
  ;Keep these lines before any File command
  ;Only for solid compression (by default, solid compression is enabled for BZIP2 and LZMA)
  
  ReserveFile "ihm.ini"
  !insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

;--------------------------------
;Installer Sections

Section "Zabbix Agent (required)" SEC01
  
  SectionIn RO
  
  ; Zabbix binaries & config file
  SetOutPath "$INSTDIR"
  strcmp $OS64B '0' 0 x64Bitinst
    File ".\Installer\win32\zabbix_agentd.exe"
    goto s1
  x64Bitinst:
    File ".\Installer\win64\zabbix_agentd.exe"
  s1:
  File ".\Installer\zabbix_agentd.conf"
  ; Zabbix docs & license
  File ".\Installer\docs\*"
  copyfiles /SILENT "$EXEDIR\scripts\*.*" "$INSTDIR"
  ; Read user input options
  !insertmacro MUI_INSTALLOPTIONS_READ $SERVER "ihm.ini" "Field 2" "State"
  !insertmacro MUI_INSTALLOPTIONS_READ $HOST   "ihm.ini" "Field 6" "State"
  !insertmacro MUI_INSTALLOPTIONS_READ $RMTCMD "ihm.ini" "Field 7" "State"
      
  ; Puts some info based on host in config file
  ${ConfigWrite} '$INSTDIR\zabbix_agentd.conf' 'Server=' '$SERVER' $OUT
  ${ConfigWrite} '$INSTDIR\zabbix_agentd.conf' 'Hostname=' '$HOST' $OUT
  ${ConfigWrite} '$INSTDIR\zabbix_agentd.conf' 'EnableRemoteCommands=' '$RMTCMD' $OUT
  ${ConfigWrite} '$INSTDIR\zabbix_agentd.conf' 'LogFile=' '$INSTDIR\zabbix_agentd.log' $OUT
  ${ConfigWrite} '$INSTDIR\zabbix_agentd.conf' '#PidFile=' '$INSTDIR\zabbix_agentd.pid' $OUT
  s32:
      
    DetailPrint "ZABBIXエージェントをサービスに登録しています..."
    nsExec::ExecTolog '"$INSTDIR\zabbix_agentd.exe" --config "$INSTDIR\zabbix_agentd.conf" --install'
    pop $0
    
    strcmp $0 '0' 0 s2
     
    DetailPrint "ZABBIXエージェントを起動しています..."
    nsExec::ExecTolog '"$INSTDIR\zabbix_agentd.exe" --config "$INSTDIR\zabbix_agentd.conf" --start'
    goto S3
    S2:
    DetailPrint "ZABBIXエージェントのインストールにエラーが発生しました"
    strcmp $OS64B '0' S3 0
    DetailPrint "Perhaps, Itanium system trying Sytem32 Agent"
    Delete "$INSTDIR\zabbix_agentd.exe"
    File ".\Installer\win32\zabbix_agentd.exe"
    goto s32
    S3:
  ; Write the installation path into the registry
  WriteRegStr HKLM "SOFTWARE\${NAME}" "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "DisplayName" "${NAME} ${DISPLAY_NAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

Section "Zabbix Sender (optional)" SEC02
  SetOutPath "$INSTDIR"
  ; ADD FILES
  DetailPrint "ZABBIX Senderをインストールしています..."
  File ".\Installer\win32\zabbix_sender.exe"
SectionEnd

Section "Zabbix get (optional)" SEC03
  SetOutPath "$INSTDIR"  
  ; ADD FILES
  DetailPrint "ZABBIX getをインストールしています..."
  File ".\Installer\win32\zabbix_get.exe"
SectionEnd

;--------------------------------
; Descriptions

LangString DESC_SEC01 ${LANG_ENGLISH} "Windows(32または64ビット)用の${NAME}をインストールします"
LangString DESC_SEC02 ${LANG_ENGLISH} "コマンドラインからデータを送信するZABBIX Senderをインストールします"
LangString DESC_SEC03 ${LANG_ENGLISH} "ZABBIXエージェントからデータを取得するZABBIX getをインストールします"

!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC01} $(DESC_SEC01)
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC02} $(DESC_SEC02)
  !insertmacro MUI_DESCRIPTION_TEXT ${SEC03} $(DESC_SEC03)
!insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;InstallerOptions (custom IHM) Functions

Function .onInit
  ;Extract InstallOptions INI files
  System::Call "kernel32::GetCurrentProcess() i .s"
  System::Call "kernel32::IsWow64Process(i s, *i .r0)"
  strcpy $OS64B $0
  !insertmacro PARAMETERNAME SERVER NONE
    ; recherche du serveur en fonction du reseau
    IfFileExists '$EXEDIR\zabbixlist.csv' 0 onInitEtap0
      SetOutPath $TEMP
      file 'Include\CheckNetwork.vbs'
      copyfiles /SILENT '$EXEDIR\zabbixlist.csv' '$TEMP\zabbixlist.csv'
      nsExec::Exec  'cscript $TEMP\CheckNetwork.vbs'

      ClearErrors
      IfFileExists '$TEMP\ZabbixServer' 0 onInitEtap0
        FileOpen $0 '$TEMP\ZabbixServer' r
        IfErrors onInitEtap0
        FileRead $0 $SERVER
        FileClose $0
   onInitEtap0:
       iffileexists  '$TEMP\ZabbixServer' 0 onInitEtap001
       delete '$TEMP\ZabbixServer'
   onInitEtap001:
      iffileexists  '$TEMP\zabbixlist.csv' 0 onInitEtap002
      delete '$TEMP\zabbixlist.csv'
  onInitEtap002:
  
  !insertmacro MUI_INSTALLOPTIONS_EXTRACT "ihm.ini"
  
  ifsilent 0 OninitOK
   strcmp $SERVER 'NONE' 0 OninitOK
   Abort
   OninitOK:
  !insertmacro PARAMETERNAME RMTCMD 0
   StrCmp $RMTCMD 1 onInitEtap1 0
   strcpy $RMTCMD 0
  onInitEtap1:
   ReadEnvStr $TMPHOST COMPUTERNAME
  
     
   ${StrCase} $HOST $TMPHOST "L"
  
  !insertmacro MUI_INSTALLOPTIONS_WRITE "ihm.ini" "Field 2" "State" $SERVER
  !insertmacro MUI_INSTALLOPTIONS_WRITE "ihm.ini" "Field 6" "State" $HOST
  !insertmacro MUI_INSTALLOPTIONS_WRITE "ihm.ini" "Field 7" "State" $RMTCMD
  
  ; Uninstall if exist
   ReadRegStr $R0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "UninstallString"
   StrCmp $R0 "" onIniTCont
   ifsilent onIniUnsint
     MessageBox MB_OKCANCEL|MB_ICONEXCLAMATION "${NAME} はすでにインストールされています。$\n$\n「OK」をクリックするとインストールされているZABBIXエージェントを削除してインストールを継続します。$\n「キャンセル」をクリックするとインストールを中止します。" IDOK onIniUnsint
     Abort   
  onIniUnsint:
    ExecWait '$R0 /S _?=$INSTDIR'
  onIniTCont:

FunctionEnd

LangString TEXT_IO_TITLE ${LANG_ENGLISH} "Configuration"
LangString TEXT_IO_SUBTITLE ${LANG_ENGLISH} "Set some options in the config file."

Function ConfigOptions
  ; Read value from %COMPUTERNAME% environment variable and store it in $HOST variable
  !insertmacro PARAMETERNAME SERVER NONE
  !insertmacro PARAMETERNAME RMTCMD 0
   StrCmp $RMTCMD 1 ConfigOptionsEtap1 0
   strcpy $RMTCMD 0
   ConfigOptionsEtap1:
   ReadEnvStr $TMPHOST COMPUTERNAME
   ${StrCase} $HOST $TMPHOST "L"
  !insertmacro MUI_HEADER_TEXT "$(TEXT_IO_TITLE)" "$(TEXT_IO_SUBTITLE)"
  ; Show default or detected value
  ; recherche du serveur en fonction du reseau
    IfFileExists '$EXEDIR\zabbixlist.csv' 0 ConfigOptionsEtape2
      SetOutPath $TEMP
      file 'Include\CheckNetwork.vbs'
      copyfiles /SILENT '$EXEDIR\zabbixlist.csv' '$TEMP\zabbixlist.csv'
      nsExec::Exec  'cscript $TEMP\CheckNetwork.vbs'

      ClearErrors
      IfFileExists '$TEMP\ZabbixServer' 0 ConfigOptionsEtape2
        FileOpen $0 '$TEMP\ZabbixServer' r
        IfErrors ConfigOptionsEtape2
        FileRead $0 $SERVER
        FileClose $0
        
   ConfigOptionsEtape2:
      iffileexists  '$TEMP\ZabbixServer' 0 ConfigOptionsEtape3
      delete '$TEMP\ZabbixServer'
   ConfigOptionsEtape3: 
   iffileexists  '$TEMP\zabbixlist.csv' 0 ConfigOptionsEtape4
      delete '$TEMP\zabbixlist.csv'
  ConfigOptionsEtape4:
  !insertmacro MUI_INSTALLOPTIONS_WRITE "ihm.ini" "Field 6" "State" $HOST
  !insertmacro MUI_INSTALLOPTIONS_WRITE "ihm.ini" "Field 2" "State" $SERVER
  !insertmacro MUI_INSTALLOPTIONS_WRITE "ihm.ini" "Field 7" "State" $RMTCMD
  ; Show custom page
  !insertmacro MUI_INSTALLOPTIONS_DISPLAY "ihm.ini"
FunctionEnd

;--------------------------------
; Uninstaller

UninstallText "This will uninstall ${NAME}. Hit next to continue."

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}"
  DeleteRegKey HKLM "SOFTWARE\${NAME}"
  ; Stop and remove Zabbix Agent service
    DetailPrint "ZABBIXエージェントのサービスを停止しています..."
    nsExec::ExecToLog  '"$INSTDIR\zabbix_agentd.exe" --config "$INSTDIR\zabbix_agentd.conf" --stop'
    DetailPrint "ZABBIXエージェントを削除しています..."
    nsExec::ExecToLog  '"$INSTDIR\zabbix_agentd.exe" --config "$INSTDIR\zabbix_agentd.conf" --uninstall  '
    
  ; Remove files and uninstaller
  Sleep 2000
  ;Delete "$INSTDIR\*"
  Delete "$INSTDIR\Zabbix_agentd.pid"
  Delete "$INSTDIR\LICENSE.txt"
  Delete "$INSTDIR\README.txt"
  Delete "$INSTDIR\zabbix_agentd.conf"
  Delete "$INSTDIR\zabbix_agentd.exe"
  Delete "$INSTDIR\zabbix_get.exe"
  Delete "$INSTDIR\zabbix_sender.exe"
  Delete "$INSTDIR\uninstall.exe"
  ${un.DirState} "$INSTDIR" $R0
  strcmp $R0 '0' 0 +2
    RMDir "$INSTDIR"

SectionEnd

