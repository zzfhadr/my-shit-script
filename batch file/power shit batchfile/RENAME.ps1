dir | rename-item -NewName {$_.name -replace "MY",""} 
dir config.log | Rename-Item -NewName { $_.name.Substring($_.name.Length -5) }
dir config.log | Rename-Item -NewName { $_.name.split(‘.’)[0] } 
dir config.log | Rename-Item -NewName { $_.name.split(‘.’)[-1] } 