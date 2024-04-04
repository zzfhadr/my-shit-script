echo 0 > test.txt
FOR /L %%y IN (1, 1, 1346) DO  call :processline %%y
goto :eof
:processline
FOR /F "tokens=1* delims=, " %%A in (test.txt) do set linlin=%%A 
IF /I %linlin% EQU 100  shutdown /s 
call called.bat
:eof


