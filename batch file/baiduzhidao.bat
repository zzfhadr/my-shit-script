@rem https://zhidao.baidu.com/question/1952349373008089068.html
set "SourDir=C:\Users\JR\OneDrive\中转\kenn\新建文件夹\new"
 
for  /f "delims=" %%a in ('powershell -c "dir %SourDir% -Recurse|sort-object{[int]($_.basename.split('.')[0])}|foreach-object{$_.fullname} "') do (
echo %%a
)