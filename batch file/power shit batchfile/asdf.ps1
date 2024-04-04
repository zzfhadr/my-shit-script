

$shell = New-Object -COMObject Shell.Application
$folder = Split-Path $path
$file = Split-Path $path -Leaf
$shellfolder = $shell.Namespace($folder)
$shellfile = $shellfolder.ParseName($file)
$shellfolder.GetDetailsOf($shellfile, 13) >> name.txt
echo " - " >> name.txt
$shellfolder.GetDetailsOf($shellfile, 21) >> name.txt
