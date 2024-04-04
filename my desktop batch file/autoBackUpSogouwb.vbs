Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "D:\desktop\LOOMING\Desktop\back up sogouwb.bat" & Chr(34), 0
Set WinScriptHost = Nothing
WScript.Quit
