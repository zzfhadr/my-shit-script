<#
.Coyp From
https://stackoverflow.com/questions/49505083/renaming-files-from-a-text-list-using-powershell
$BasePath = 'C:\Test'
$FilesToChangeFolderName = 'extractedFiles1'
$filestochange = Get-ChildItem -Path "$BasePath\$FilesToChangeFolderName"

$FileNames = Get-Content "$BasePath\outputfile.txt"

if($filestochange.FullName.Count -eq $FileNames.Count)
{
    for($i=0; $i -lt $FileNames.Count; $i++)
    {
        write-host "Renaming file $($filestochange.Name[$i]) to $($FileNames[$i]+".txt")"
        Rename-Item -Path $filestochange.FullName[$i] -NewName ($FileNames[$i]+".txt")
    }
}
#>

$BasePath = 'D:\desktop\LOOMING\Desktop\x'
$FilesToChangeFolderName = 'renamed'
$filestochange = Get-ChildItem -Path "$BasePath\$FilesToChangeFolderName"

$FileNames = Get-Content "$BasePath\list.txt"
$Filename = Get-Content "$BasePath\name.txt"
if($filestochange.FullName.Count -eq $FileNames.Count*2)
{
    for($i=0; $i -lt $FileNames.Count; $i++)
    {
        write-host "Renaming file $($Filename[$i]) to $($FileNames[$i])"
        Rename-Item -Path ($BasePath+'\'+$FilesToChangeFolderName+'\'+$Filename[$i]+".dff") -NewName ($FileNames[$i]+".dff")
        Rename-Item -Path ($BasePath+'\'+$FilesToChangeFolderName+'\'+$Filename[$i]+".txd") -NewName ($FileNames[$i]+".txd")
    }
}