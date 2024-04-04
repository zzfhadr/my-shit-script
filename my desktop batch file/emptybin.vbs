Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "D:\desktop\LOOMING\Desktop\empty recycle bin.bat" & Chr(34), 0
Set WinScriptHost = Nothing
WScript.Quit
