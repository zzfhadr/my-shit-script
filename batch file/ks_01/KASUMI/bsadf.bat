
 @rem not necessary get rid of this can see dug info???
CHCP 936
del D:\desktop\LOOMING\Desktop\ks_01\KASUMI\TEMPJP.txt D:\desktop\LOOMING\Desktop\ks_01\KASUMI\TEMPCH.txt
@rem del D:\desktop\LOOMING\Desktop\ks_01\KASUMI\*555.txt
@rem set /p "filename=Enter name: "
echo It's fine above
dir /B /O:n *.s > D:\desktop\LOOMING\Desktop\ks_01\KASUMI\tempfile.txt
for /F "usebackq  tokens=1* delims=" %%B in (D:\desktop\LOOMING\Desktop\ks_01\KASUMI\tempfile.txt) do set filelinlin=%%B & call :toaaa %%B
goto :eof
:toaaa
for /F "usebackq  tokens=1* " %%A in ("D:\desktop\LOOMING\Desktop\ks_01\KASUMI\%filelinlin%") do set linlin=%%A & call :processline %%A

@rem pause
goto :eof
:processline
set bolblobl=F
if /I "%linlin:~0,1%" EQU "^" (
	if /I "%linlin:~1,1%" NEQ "s" (	set bolblobl=T)
	IF /I "%linlin:~2,1%" NEQ "e" (	IF /I "%linlin:~2,1%" NEQ "a" (   set bolblobl=T)	)
	IF /I "%linlin:~1,1%" NEQ "s" (	IF /I "%linlin:~2,1%" NEQ "e" (   set bolblobl=T)	)
	IF /I "%linlin:~1,1%" NEQ "s"(	IF /I "%linlin:~2,1%" NEQ "a" (   set bolblobl=T)	)
	) 
if "%linlin:~0,1%"=="“" (
	set bolblobl=T
	) 
if "%linlin:~0,1%"=="y" (
	set bolblobl=T
	) 
if "%linlin:~0,1%"=="\" (
	set bolblobl=T
	) 
if "%bolblobl%"=="T" 	(
	
	echo ^%linlin% > D:\desktop\LOOMING\Desktop\ks_01\KASUMI\TEMPJP.txt	
	iconv.lnk -c  -f  SHIFT-JIS -t GBK  D:\desktop\LOOMING\Desktop\ks_01\KASUMI\TEMPJP.txt >> D:\desktop\LOOMING\Desktop\ks_01\KASUMI\Conv%filelinlin:~0,-2%
	goto :eof
	)
echo %linlin% >> D:\desktop\LOOMING\Desktop\ks_01\KASUMI\Conv%filelinlin:~0,-2%
@rem echo %linlin% > TEMPCH.txt
@rem iconv.lnk -c -f  GBK -t UTF-8 D:\desktop\LOOMING\Desktop\ks_01\KASUMI\TEMPCH.txt >> D:\desktop\LOOMING\Desktop\ks_01\KASUMI\555.txt

:eof
