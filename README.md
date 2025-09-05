
# API FastAPI - Exemplo Simples

Esta API foi desenvolvida em Python utilizando o framework FastAPI.

## Endpoints

- `/` ou `/health`: Verifica se a API está funcionando.
- `/me`: Retorna informações pessoais do aluno.


1. **Clona o repositório:**
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio
   ```

2. **Cria e ativa um ambiente virtual:**
   ```bash
   python -m venv .venv
   # Ative no Windows:
   .venv\Scripts\activate
   # Ative no Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instala as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura o arquivo `.env`**:
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

5. **Executa a API localmente:**
   ```bash
   uvicorn app.main:app --reload
   ```
   Acesse: http://127.0.0.1:8000/


6.Configuro o Render para poder lê a API

   **Meu link no Render **
   https://api-1-ikdc.onrender.com
