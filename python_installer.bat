::Note: This isn't mine.
::Credits for this go to github/KDot227
@echo off

echo Made by K.Dot for Python kids and skids

@echo off
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)

:got_admin
echo $html = Invoke-WebRequest -Uri "https://www.python.org/downloads" -UseBasicParsing > worker.ps1
echo $newest_version = $html.Links ^| Where-Object {$_.href -like "https://www.python.org/ftp/python/*/python-*amd64.exe"} ^| Select-Object -Last 1 -ExpandProperty href >> worker.ps1
echo $ver = $newest_version -replace "https://www.python.org/ftp/python/", "" -replace "/python-.*", "" >> worker.ps1
echo.  >> worker.ps1
echo #Made by https://github.com/KDot227 >> worker.ps1
echo.  >> worker.ps1
echo try { >> worker.ps1
echo     python.exe --version >> worker.ps1
echo     $status = "Working" >> worker.ps1
echo     Start-Sleep -s 3 >> worker.ps1
echo     EXIT >> worker.ps1
echo } >> worker.ps1
echo catch { >> worker.ps1
echo     $status = "Not Working" >> worker.ps1
echo } >> worker.ps1
echo.  >> worker.ps1
echo if ($status -eq "Working") { >> worker.ps1
echo     Write-Host "Python is working and added to path" >> worker.ps1
echo     Start-Sleep -s 3 >> worker.ps1
echo     EXIT >> worker.ps1
echo } >> worker.ps1
echo else { >> worker.ps1
echo     $python_maybe = Test-Path -Path "C:\Users\$env:username\AppData\Local\Programs\Python\*\python.exe" -ErrorAction SilentlyContinue >> worker.ps1
echo     if ($python_maybe) { >> worker.ps1
echo         Write-Host "Python is installed but not added to path" >> worker.ps1
echo         $python_path = where.exe /R c:\Users\$env:UserName\AppData\Local\Programs\Python python.exe >> worker.ps1
echo         try { >> worker.ps1
echo             Write-Host $python_path[0] >> worker.ps1
echo             $real = ( Get-ChildItem "C:\Users\$env:username\AppData\Local\Programs\Python" -Depth 1 -Recurse -Directory -Filter 'Scripts' ).FullName >> worker.ps1
echo             $exe_python = ( Get-ChildItem "C:\Users\$env:username\AppData\Local\Programs\Python" -Directory -Filter '' ).FullName >> worker.ps1
echo             try { >> worker.ps1
echo                 [Environment]::SetEnvironmentVariable("Path", $env:Path + ";$exe_python;$real", "User") >> worker.ps1
echo                 Write-Host "Python added to path" >> worker.ps1
echo                 Start-Sleep -s 1 >> worker.ps1
echo             } >> worker.ps1
echo             catch { >> worker.ps1
echo                 Write-Host issue with adding python to path!!! >> worker.ps1
echo                 Start-Sleep -s 1 >> worker.ps1
echo             } >> worker.ps1
echo         } >> worker.ps1
echo         catch { >> worker.ps1
echo             Write-Host "AN ERROR OCCURED" >> worker.ps1
echo             Start-Sleep -s 3 >> worker.ps1
echo             EXIT >> worker.ps1
echo         } >> worker.ps1
echo     } >> worker.ps1
echo     else { >> worker.ps1
echo         Write-Host "Python is not installed" >> worker.ps1
echo         Write-Host "DOWNLOADING PYTHON" >> worker.ps1
echo.  >> worker.ps1
echo         [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 >> worker.ps1
echo.  >> worker.ps1
echo         Invoke-WebRequest -Uri "https://www.python.org/ftp/python/$ver/python-$ver-amd64.exe" -UseBasicParsing -Outfile $env:TEMP/python-setup.exe >> worker.ps1
echo.  >> worker.ps1
echo         Start-Process "cmd.exe" -ArgumentList "/c echo INSTALLING PYTHON DO NOT CLOSE & $env:TEMP\python-setup.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait >> worker.ps1
echo.  >> worker.ps1
echo         Remove-Item $env:TEMP/python-setup.exe -Force >> worker.ps1
echo         } >> worker.ps1
echo } >> worker.ps1
powershell.exe -ExecutionPolicy Bypass -File worker.ps1
del worker.ps1
exit
