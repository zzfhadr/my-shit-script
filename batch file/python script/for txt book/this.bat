FOR /L %%y IN (1, 1, 108) DO (
FOR /F "tokens=1* delims=, " %%A in (test.txt) do set linlin=%%A 
IF /I "%linlin%" EQU "100" goto :eof
call called.bat
	)


