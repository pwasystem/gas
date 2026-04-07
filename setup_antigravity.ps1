# setup_antigravity.ps1
Write-Host "🚀 Iniciando Configuração do Google Antigravity para Windows..." -ForegroundColor Cyan

# 1. Verificar Node.js
if (Get-Command node -ErrorAction SilentlyContinue) {
    Write-Host "✅ Node.js detectado." -ForegroundColor Green
} else {
    Write-Host "❌ Erro: Node.js não encontrado. Baixe em https://nodejs.org/" -ForegroundColor Red
    exit
}

# 2. Instalar Clasp globalmente
Write-Host "📦 Instalando Google Clasp via NPM..." -ForegroundColor Yellow
npm install -g @google/clasp

# 3. Verificar Python e instalar dependências do MCP
if (Get-Command python -ErrorAction SilentlyContinue) {
    Write-Host "🐍 Instalando dependências Python (mcp, fastmcp)..." -ForegroundColor Yellow
    pip install mcp fastmcp
} else {
    Write-Host "⚠️ Python não encontrado no PATH. Instale o Python para rodar o servidor MCP." -ForegroundColor Yellow
}

# 4. Habilitar a API
Write-Host "🔗 Abrindo configurações do Apps Script. Certifique-se de que a API está 'ON'." -ForegroundColor Cyan
Start-Process "https://script.google.com/home/settings"

Write-Host "✅ Ambiente preparado para o Google Antigravity!" -ForegroundColor Green