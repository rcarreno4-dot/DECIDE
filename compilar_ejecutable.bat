@echo off
title Compilar DECIDE v2.0 a Ejecutable Windows (.exe)
cd /d %~dp0

echo ===================================================================
echo     Compilando DECIDE v2.0 con PyInstaller a archivo .exe
echo ===================================================================
echo.

python -m PyInstaller --noconfirm --clean ^
    --name "DECIDE_v2" ^
    --onefile ^
    --add-data "web;web" ^
    --add-data "decide_datos.db;." ^
    lanzador_app.py

echo.
if exist "dist\DECIDE_v2.exe" (
    echo ===================================================================
    echo   [EXITO] El ejecutable ha sido generado exitosamente:
    echo   dist\DECIDE_v2.exe
    echo ===================================================================
) else (
    echo [ERROR] Ocurrio un problema durante la compilacion.
)
pause
