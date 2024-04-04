@echo off
title Kill not windows app
cd c:\windows\System32
for /f "skip=3 tokens=1 delims=." %%i in ('TASKLIST /FI "USERNAME eq %userdomain%\%username%" /FI "STATUS eq running"') do (
if not "%%i.exe"=="AsMonStartupTask64.exe  " (
if not "%%i.exe"=="sihost.exe" (
if not "%%i.exe"=="taskhostw.exe" (
if not "%%i.exe"=="ASUSDisplayCtrl.exe" (
if not "%%i.exe"=="ASUS_FRQ_Control.exe" (
if not "%%i.exe"=="ctfmon.exe" (
if not "%%i.exe"=="igfxEM.exe" (
if not "%%i.exe"=="StartMenuExperienceHost.exe" (
if not "%%i.exe"=="SearchApp.exe" (
if not "%%i.exe"=="RuntimeBroker.exe" (
if not "%%i.exe"=="igfxext.exe" (
if not "%%i.exe"=="RuntimeBroker.exe" (
if not "%%i.exe"=="TextInputHost.exe" (
if not "%%i.exe"=="dllhost.exe" (
if not "%%i.exe"=="smartscreen.exe" (
if not "%%i.exe"=="conhost.exe" (
if not "%%i.exe"=="SecurityHealthSystray.exe" (
if not "%%i.exe"=="OneDrive.exe" (
if not "%%i.exe"=="Microsoft.exe" (
if not "%%i.exe"=="Clash for Windows.exe" (
if not "%%i.exe"=="HControl.exe" (
if not "%%i.exe"=="backgroundTaskHost.exe" (
if not "%%i.exe"=="RtkAudUService64.exe" (
if not "%%i.exe"=="svchost.exe" (
if not "%%i.exe"=="explorer.exe" (
if not "%%i.exe"=="cmd.exe" (
if not "%%i.exe"=="tasklist.exe" (
if not "%%i.exe"=="ATKOSD2.exe" (
if not "%%i.exe"=="AsusSoftwareManagerAgent.exe" (
echo.
taskkill /f /im "%%i.exe" 
echo.
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)
)

