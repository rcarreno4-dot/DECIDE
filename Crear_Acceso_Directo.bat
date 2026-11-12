@echo off
title Crear Acceso Directo de DECIDE v2.0
cd /d %~dp0

set "TARGET=%~dp0dist\DECIDE_v2.exe"
if not exist "%TARGET%" set "TARGET=%~dp0DECIDE_v2.exe"

if not exist "%TARGET%" (
    echo [ERROR] No se encontro el archivo DECIDE_v2.exe
    echo Primero compila el ejecutable con compilar_ejecutable.bat
    pause
    exit /b
)

echo Creando acceso directo en el Escritorio...
powershell -NoProfile -Command "$ws = New-Object -ComObject WScript.Shell; $desktop = [Environment]::GetFolderPath('Desktop'); $s = $ws.CreateShortcut($desktop + '\DECIDE v2.0.lnk'); $s.TargetPath = '%TARGET%'; $s.WorkingDirectory = Split-Path '%TARGET%'; $s.Save(); Write-Host 'Acceso directo creado en:' ($desktop + '\DECIDE v2.0.lnk')"

echo.
echo ===================================================================
echo   [EXITO] Acceso directo 'DECIDE v2.0' creado en tu Escritorio!
echo   Ya puedes abrir DECIDE directamente desde tu Escritorio.
echo ===================================================================
pause
