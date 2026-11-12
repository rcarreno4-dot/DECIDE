@echo off
chcp 65001 >nul
title DECIDE v2.0 - Evaluador de Competencias Emocionales
cd /d "%~dp0"
echo ========================================================
echo   Iniciando DECIDE v2.0 - Entorno Web y de Escritorio
echo ========================================================
python lanzador_app.py
pause
