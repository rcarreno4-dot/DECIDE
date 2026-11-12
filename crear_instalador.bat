@echo off
title Generador del Instalador Oficial de DECIDE v2.0
cd /d %~dp0

echo ===================================================================
echo     Generando Instalador Oficial de DECIDE v2.0
echo ===================================================================
echo.

echo 1. Compilando aplicacion DECIDE en modo ventana (sin consola CMD)...
python -m PyInstaller --noconfirm --clean ^
    --name "DECIDE_v2" ^
    --windowed ^
    --add-data "web;web" ^
    --add-data "decide_datos.db;." ^
    lanzador_app.py

if not exist "dist\DECIDE_v2\DECIDE_v2.exe" (
    echo [ERROR] Fallo la compilacion de la aplicacion base.
    pause
    exit /b
)

echo.
echo 2. Empaquetando archivos del sistema en app_payload.zip...
python -c "import shutil; shutil.make_archive('app_payload', 'zip', 'dist/DECIDE_v2')"

echo.
echo 3. Compilando el Asistente de Instalacion Grafico (Instalador_DECIDE_v2.exe)...
python -m PyInstaller --noconfirm --clean ^
    --name "Instalador_DECIDE_v2" ^
    --onefile ^
    --windowed ^
    --add-data "app_payload.zip;." ^
    instalador_gui.py

if exist "dist\Instalador_DECIDE_v2.exe" (
    copy /y "dist\Instalador_DECIDE_v2.exe" "Instalador_DECIDE_v2.exe" >nul
    echo.
    echo ===================================================================
    echo   [EXITO] Instalador generado exitosamente:
    echo   Instalador_DECIDE_v2.exe
    echo ===================================================================
) else (
    echo [ERROR] No se pudo generar el instalador.
)
pause
