#!/bin/bash

# Ejecutar el comando pip
.venv/Scripts/pip "$@"

# Actualizar requirements.txt después de ejecutar el comando pip
.venv/Scripts/pip freeze > requirements.txt
