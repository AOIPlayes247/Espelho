@echo off
chcp 65001 >nul
title StarControl PC
cd /d "%~dp0"
set PY=python
where py >nul 2>nul && set PY=py
%PY% --version >nul 2>nul || (echo Python nao encontrado. Instale em https://www.python.org/downloads/ marcando "Add Python to PATH". & pause & exit /b 1)
%PY% -c "import websockets,pydirectinput,pynput" >nul 2>nul || (echo Instalando dependencias... & %PY% -m pip install websockets pydirectinput pynput)
:run
echo Iniciando StarControl... (feche esta janela para parar)
%PY% agent.py
echo.
echo O agente parou. Reiniciando em 3 segundos...
timeout /t 3 >nul
goto run
