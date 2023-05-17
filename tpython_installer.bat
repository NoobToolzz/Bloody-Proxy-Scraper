::Not made by me, taken from addi00000/empyrean repository
::Name is tpython_installer because I want it to be at the bottom of the folder (If you assort them by file name)
@echo off

for /f "tokens=1,2 delims= " %%a in ('powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/ -UseBasicParsing | Select-String -Pattern '3.10.[0-9]{1,2}' -AllMatches | Select-Object -ExpandProperty Matches | Select-Object -ExpandProperty Value | Sort-Object -Descending -Unique | Select-Object -First 1"') do (
    set "PYTHON_VERSION=%%a%%b"
)
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
set "PYTHON_EXE=python-installer.exe"

curl -L -o %PYTHON_EXE% %PYTHON_URL%

start /wait %PYTHON_EXE% /quiet /passive InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1 Include_doc=0

del %PYTHON_EXE%
