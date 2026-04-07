#!/bin/bash

echo "🚀 Iniciando Configuração do Google Antigravity..."

# 1. Verificar Node.js (necessário para o clasp)
if ! command -v node &> /dev/null; then
    echo "❌ Erro: Node.js não encontrado. Instale-o primeiro."
    exit 1
fi

# 2. Instalar Clasp globalmente
echo "📦 Instalando Google Clasp..."
npm install -g @google/clasp

# 3. Instalar dependências Python para o MCP
echo "🐍 Instalando dependências do servidor MCP..."
pip install mcp fastmcp

# 4. Habilitar a API do Apps Script (abre o link no navegador)
echo "🔗 Por favor, garanta que a API está ATIVADA em: https://script.google.com/home/settings"
echo "✅ Ambiente preparado!"