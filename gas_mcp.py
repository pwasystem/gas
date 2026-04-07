import os
import subprocess
from typing import List, Dict, Union, Optional
from mcp.server.fastmcp import FastMCP
from pathlib import Path

# Inicializa o servidor FastMCP
mcp = FastMCP(
    "Google-Antigravity",
    instructions="Servidor MCP para automação total de projetos Google Apps Script via clasp."
)

# --- FERRAMENTAS DE AUTOMAÇÃO CLASP ---

def executar_clasp(comando: List[str]) -> str:
    """Função auxiliar para executar comandos shell com segurança."""
    try:
        resultado = subprocess.run(
            comando, 
            capture_output=True, 
            text=True, 
            check=True,
            shell=False # Segurança: evita injeção de comandos
        )
        return f"Sucesso:\n{resultado.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar comando: {e.stderr}"
    except FileNotFoundError:
        return "Erro: O comando 'clasp' não foi encontrado. Certifique-se de que o clasp está instalado globalmente (npm install -g @google/clasp)."

@mcp.tool()
def GasLogin() -> str:
    """
    Realiza a autenticação no Google Apps Script. 
    Atenção: Isso abrirá uma janela no navegador para login via OAuth2.
    """
    return executar_clasp(["clasp", "login"])

@mcp.tool()
def GasCriar(nome_projeto: str, tipo_projeto: str = "standalone") -> str:
    """
    Cria um novo projeto do Apps Script localmente.
    Tipos válidos: standalone, docs, sheets, slides, forms, webapp, api.
    """
    return executar_clasp(["clasp", "create", "--title", nome_projeto, "--type", tipo_projeto])

@mcp.tool()
def GasAbrir(script_id: str) -> str:
    """
    Clona um projeto existente do Google Apps Script para a pasta local usando o ID do Script.
    """
    return executar_clasp(["clasp", "clone", script_id])

@mcp.tool()
def GasEnviar() -> str:
    """
    Envia (push) o código local para o servidor do Google Apps Script. 
    Atenção: Sobrescreve o código no editor online.
    """
    return executar_clasp(["clasp", "push"])

@mcp.tool()
def GasBaixar() -> str:
    """
    Baixa (pull) a versão mais recente do código do servidor para o ambiente local.
    """
    return executar_clasp(["clasp", "pull"])

# --- FERRAMENTAS DE LEITURA E DOCUMENTAÇÃO (MANTIDAS) ---

@mcp.tool()
def listar_arquivos_gas(diretorio_src: str = "src") -> str:
    """Lista arquivos .js, .ts, .html e .json no diretório de origem."""
    try:
        base_path = Path(diretorio_src)
        if not base_path.exists():
            return f"Erro: Diretório '{diretorio_src}' não encontrado."

        arquivos = []
        for root, dirs, files in os.walk(base_path):
            dirs[:] = [d for d in dirs if d not in {".git", "node_modules"}]
            for file in files:
                if Path(file).suffix.lower() in {".js", ".ts", ".html", ".json"}:
                    arquivos.append(os.path.relpath(os.path.join(root, file)))

        return "Arquivos encontrados:\n" + "\n".join(arquivos) if arquivos else "Nenhum arquivo encontrado."
    except Exception as e:
        return f"Erro: {str(e)}"

@mcp.tool()
def ler_codigo_gas(caminho_arquivo: str) -> str:
    """Lê o conteúdo de um arquivo específico do projeto."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return f"--- Conteúdo de {caminho_arquivo} ---\n\n{f.read()}"
    except Exception as e:
        return f"Erro ao ler arquivo: {str(e)}"

if __name__ == "__main__":
    mcp.run()