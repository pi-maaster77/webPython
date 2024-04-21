@echo off
REM Ejecutar el comando pip
.venv\Scripts\python -m pip %*

REM Actualizar requirements.txt después de ejecutar el comando pip
.venv\Scripts\python -m pip freeze > requirements.txt
