# Google-Antigravity MCP para Google Apps Script (GAS)

Este é um Servidor MCP (Model Context Protocol) construído com FastMCP, desenhado para permitir a automação e gestão de projetos no Google Apps Script diretamente do seu LLM ou cliente compatível com MCP. O servidor utiliza o `clasp` (Command Line Apps Script Projects) por trás para interagir com o ambiente do Google.

## 📋 Pré-requisitos

Para que o servidor MCP funcione corretamente, o seu ambiente precisará ter:
- **Node.js** instalado (para gerenciar o pacote `clasp`).
- **Python 3** instalado no PATH (para executar o servidor MCP).
- **Conta Google** com acesso ao Google Apps Script.

## 🚀 Instalação e Configuração

O projeto inclui scripts automatizados de instalação para diferentes sistemas operacionais. Escolha o que se adequa ao seu ambiente:

- **Windows (PowerShell):** Execute `./setup_antigravity.ps1`
- **Windows (Prompt de Comando):** Execute `setup_antigravity.bat`
- **Linux / macOS:** Execute `./setup_antigravity.sh` (Não se esqueça de dar permissões de execução com `chmod +x`)

Esses scripts farão o seguinte:
1. Validar a instalação do Node.js.
2. Instalar o `@google/clasp` globalmente.
3. Instalar os pacotes Python necessários (`mcp` e `fastmcp`).
4. Abrir automaticamente a página de configurações do Apps Script.

> [!IMPORTANT]  
> Você deve acessar a [Página de Configurações do Google Apps Script](https://script.google.com/home/settings) e garantir que a opção **"Google Apps Script API"** esteja **ativada (ON)**. O Clasp não funcionará se a API estiver desativada.

## ⚙️ Integrando no seu Client MCP (ex: Claude Desktop)

Você precisa apontar as configurações do seu cliente MCP para o script principal `gas_mcp.py`. Exemplo de configuração (como no `claude_desktop_config.json` ou similar):

```json
{
  "mcpServers": {
    "google-antigravity": {
      "command": "python",
      "args": ["d:/Sistemas/mcp_gas/gas_mcp.py"]
    }
  }
}
```

*Obs: Substitua o caminho do `args` para o caminho absoluto do arquivo `gas_mcp.py` se você instalar em outro local.*

## 🛠️ Ferramentas Disponíveis

Uma vez conectado, as seguintes ferramentas MCP estarão disponíveis:

### Ferramentas do Clasp
- **`GasLogin`**: Inicia o processo de autenticação no Google Apps Script usando OAuth2. O comando abrirá uma janela no seu navegador.
- **`GasCriar(nome_projeto, tipo_projeto)`**: Cria um novo projeto do Apps Script localmente. (Tipos suportados: `standalone`, `docs`, `sheets`, `slides`, `forms`, `webapp`, `api`).
- **`GasAbrir(script_id)`**: Clona o código de um projeto existente do Google Apps Script usando o Script ID para o diretório local.
- **`GasEnviar`**: Sobrepõe o código local no servidor do Google Apps Script (`clasp push`). **Atenção:** as mudanças online sem *pull* serão apagadas.
- **`GasBaixar`**: Sincroniza e traz a versão mais atual do servidor para os arquivos locais (`clasp pull`).

### Exploração e Análise Local
- **`listar_arquivos_gas(diretorio_src)`**: Faz a varredura e lista quais os arquivos locais no projeto (`.js`, `.ts`, `.html`, `.json`), ignorando pastas desnecessárias como `node_modules` e `.git`.
- **`ler_codigo_gas(caminho_arquivo)`**: Recupera e expõe o conteúdo do script especificado para a IA ler, debugar e editar.

## 💡 Como Usar (Fluxo de Trabalho Recomendado)

1. **Autenticação:** Na sua primeira utilização, peça para a IA executar a ferramenta `GasLogin`. Complete o login no navegador e autorize o `.clasp.json` gerado.
2. **Iniciando um Projeto:** Crie (`GasCriar`) ou pegue um repositório da web (`GasAbrir` / `GasBaixar`). 
3. **Desenvolvimento Local:** Você pode usar a extensão para gerenciar as edições nos códigos locais no seu diretório. 
4. **Deploy:** Uma vez realizadas edições, utilize a ferramenta `GasEnviar` para subir as alterações ao seu script online efetivamente.
