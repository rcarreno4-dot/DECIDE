@echo off
title DECIDE v2.0 - Web Edition (React + Tailwind + Bootstrap)
cd /d %~dp0

echo ===================================================================
echo     Iniciando DECIDE v2.0 - Web Edition (React + Tailwind + Bootstrap)
echo ===================================================================
echo.
echo 1. Iniciando Servidor Web DECIDE en Python (puerto 5000)...
start "DECIDE Web Server" cmd /k "python app_web.py"

timeout /t 2 /nobreak >nul
echo.
echo 2. Abriendo navegador en http://localhost:5000 ...
start http://localhost:5000

echo.
echo Aplicacion iniciada con exito en http://localhost:5000
echo Puedes minimizar esta ventana.
