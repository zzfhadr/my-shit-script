
for /f "skip=3 tokens=1 delims=." %%i in ('TASKLIST /FI "USERNAME eq %userdomain%\%username%" /FI "STATUS eq running"  ') do (echo %%i >> al.txt  )