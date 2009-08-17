Const EnLecture = 1, EnEcriture = 2, enAppend = 8
dim oFSO,WshShell,oFichierLog
Set WshShell = WScript.CreateObject("WScript.Shell")
tempFolder = WshShell.ExpandEnvironmentStrings( "%temp%" )
if right(tempFolder,1) <> "\"  then tempFolder=tempFolder & "\"
Set oFSO = CreateObject("Scripting.FileSystemObject")  

'On Error Resume Next
Main
oFSO.deletefile (tempFolder & "CheckNetwork.vbs")
'nettoyage

Sub Main ()
  Const wbemFlagReturnImmediately = &h10
  Const wbemFlagForwardOnly = &h20
  
  'On Error Resume Next
     Set objWMIService = GetObject("winmgmts:\\.\root\CIMV2")
     Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled=TRUE", "WQL", wbemFlagReturnImmediately + wbemFlagForwardOnly)
  	   For Each objItem In colItems
  	     Min = lbound (objItem.ipaddress)
  	     Max = ubound (objItem.ipaddress)
  	     For i = Min to Max
  	        AdrIP= objItem.ipaddress(i)
  	        SubNet= objItem.IPSubnet (i)
  	        if AdrIP<>"0.0.0.0" then
  	            DIM SUBNET
  	            SUBNET =  CalcSubnet(AdrIP , SubNet)
                FindZabbix SUBNET,"zabbixlist.csv"        
  	        end if
   	     Next  
       Next
 End Sub
 
Function calcSubnet(strAddress, strMask)
  intSubnetLength = SubnetLength(strMask)
  calcSubnet = BinaryToString(Left(StringToBinary(strAddress), intSubnetLength) & String(32 - intSubnetLength, "0"))
End Function


Function SubnetLength(strMask)
  strMaskBinary = StringToBinary(strMask)
  SubnetLength = Len(Left(strMaskBinary, InStr(strMaskBinary, "0") - 1))
End Function

Function BinaryToString(strBinary)
  For intOctetPos = 1 To 4
    strOctetBinary = Right(Left(strBinary, intOctetPos * 8), 8)
    intOctet = 0
    intValue = 1
    For intBinaryPos = 1 To Len(strOctetBinary)
      If Left(Right(strOctetBinary, intBinaryPos), 1) = "1" Then intOctet = intOctet + intValue
      intValue = intValue * 2
    Next
    If BinaryToString = Empty Then BinaryToString = CStr(intOctet) Else BinaryToString = BinaryToString & "." & CStr(intOctet)
  Next
End Function

Function StringToBinary(strAddress)
  objAddress = Split(strAddress, ".", -1)
  For Each strOctet In objAddress
    intOctet = CInt(strOctet)
    strOctetBinary = ""
    For x = 1 To 8
      If intOctet Mod 2 > 0 Then
        strOctetBinary = "1" & strOctetBinary
      Else
        strOctetBinary = "0" & strOctetBinary
      End If
    intOctet = Int(intOctet / 2)
    Next
    StringToBinary = StringToBinary & strOctetBinary
  Next
End Function

function FindZabbix (Clef,FichierIN)
  dim valdef
  path = left (wscript.scriptfullname,len(wscript.scriptfullname)-len(wscript.scriptName) )
  
  If  oFSO.FileExists(path & FichierIN) Then
  	Set oFichierIn = oFSO.OpenTextFile(path & FichierIN, EnLecture)		 
  	Do While Not oFichierIn.AtEndOfStream
  		Iligne = Trim(oFichierIn.ReadLine)
  		Dim Table 
  		if instr(iligne,";")= 0 then
  		    
      else 
          table = split(iligne,";")
      		if ucase (trim (table (0))) = "DEFAULT" then 
                valdef = table (1)
          else if  ucase (trim (table (0))) = ucase(trim(Clef)) then
                   FindZabbix = ucase (trim (table (1)))
               end if
          end if
      end if
  	Loop
  	if trim(FindZabbix) <> "" then
  	 WRITEVAL FindZabbix,"ZabbixServer"
  	else
      if trim(valdef) <> "" then WRITEVAL valdef,"ZabbixServer"
    end if
  	oFichierIn.close
  	' Eciture du paramêtre
  end if
End function
 
Function WRITEVAL(VALEUR,FichierOUT)
	If oFSO.FileExists(FichierOUT) Then
			ofso.deletefile (FichierOUT)
		End If
		Set oFichierOUT = oFSO.createTextFile(FichierOUT)
		oFichierOUT.WriteLine VALEUR
		oFichierOUT.close
end function 
