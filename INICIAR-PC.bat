@echo off
chcp 65001 >nul
title StarControl PC
cd /d "%~dp0"
set PY=python
where py >nul 2>nul && set PY=py
%PY% --version >nul 2>nul || (echo Python nao encontrado. Instale em https://www.python.org/downloads/ marcando "Add Python to PATH". & pause & exit /b 1)
echo Instalando dependencias...
%PY% -m pip install --quiet --upgrade websockets pydirectinput pynput
echo Iniciando StarControl...
%PY% agent.py
pause
