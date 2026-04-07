@echo off
title Configuração Google Antigravity
echo 🚀 Iniciando configuracao para Windows...

:: 1. Verificar Node.js
node -v >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Erro: Node.js nao encontrado.
    pause
    exit /b
)

:: 2. Instalar Clasp
echo 📦 Instalando Google Clasp...
call npm install -g @google/clasp

:: 3. Instalar dependencias Python
echo 🐍 Instalando mcp e fastmcp...
python -m pip install mcp fastmcp

:: 4. Abrir link da API
echo 🔗 Abrindo configuracoes do Google Apps Script...
start https://script.google.com/home/settings

echo ✅ Concluido! O Antigravity esta pronto para decolar.
pause