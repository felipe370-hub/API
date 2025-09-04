# API FastAPI - Exemplo Simples

Esta API foi desenvolvida em Python utilizando o framework FastAPI.

## Endpoints

- `/` ou `/health`: Verifica se a API está funcionando.
- `/me`: Retorna informações pessoais do aluno.

## Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   # Ative no Windows:
   .venv\Scripts\activate
   # Ative no Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env`** (já existe um exemplo no repositório):
   ```env
   API_NAME=Minha API FastAPI
   API_VERSION=1.0.0
   API_DESCRIPTION=API simples com endpoints /health e /me
   ME_NOME=Seu Nome
   ME_EMAIL=seu.email@exemplo.com
   ME_CURSO=Seu Curso
   ME_GITHUB=https://github.com/seuusuario
   ME_CIDADE=Sua Cidade
   ME_INTERESSES=Python,APIs,FastAPI,Tecnologia
   ```

5. **Execute a API localmente:**
   ```bash
   uvicorn app.main:app --reload
   ```
   Acesse: http://127.0.0.1:8000/

## Deploy no Render

1. Faça login em [https://render.com](https://render.com) e crie um novo serviço Web.
2. Conecte seu repositório GitHub público.
3. Configure o build command:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o start command:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 10000
   ```
5. Adicione as variáveis de ambiente do `.env` no painel do Render.
6. Aguarde o deploy e copie o link público gerado.

## Link público da API no Render

> [https://seu-link-no-render.onrender.com](https://seu-link-no-render.onrender.com)

---

Se tiver dúvidas, abra uma issue ou entre em contato!
