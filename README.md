# Project Traduzo

Project Traduzo é uma aplicação web que permite a tradução de textos entre diferentes idiomas usando a API do Google Translator. Além disso, a aplicação mantém um histórico de traduções e fornece funcionalidades de administração para gerenciar esse histórico.

## Sumário

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Testes](#testes)
- [Endpoints](#endpoints)
- [Licença](#licença)

## Instalação

**[1]** Clone o repositório:

```bash
git clone https://github.com/matheusrosa1/project-traduzo.git
cd project-traduzo
```

**[2]** Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # Para sistemas Unix
venv\Scripts\activate  # Para Windows
 ```

**[3]** Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

**Escolha uma opção:**

**[4 - Opção A]** Banco e Flask pelo Docker

```bash
docker compose up translate
```

**[4 - Opção B]** Banco pelo Docker, Flask localmente pelo ambiente virtual

```bash
docker compose up -d mongodb

python3 src/app.py
```

**[5]** A aplicação automaticamente já estará disponível na rota http://127.0.0.1:8000/


## Testes

1. **Configuração para Testes:**

    - O projeto inclui fixtures para configuração do ambiente de testes, utilizando `pytest`. As fixtures limpam e preparam o banco de dados antes de cada teste.

2. **Execução dos Testes:**

<summary>Pytest pelo ambiente virtual </summary>

**[1]** Crie o ambiente virtual, e instale as dependências, suba o banco, conforme seção preparando ambiente

**[2]** Execute os testes

```bash
python3 -m pytest
```

<summary>Pytest pelo Container Docker </summary>

**[1]** Execute o projeto conforme seção preparando ambiente

**[2]** Execute os testes diretamente, ou após acessar o sh do container

```bash
docker compose exec -it translate pytest
```

## Endpoints

### Rota Principal

- `GET /` - Exibe a página de tradução.
- `POST /` - Envia um texto para tradução e retorna o resultado.

### Histórico de Traduções

- `GET /history` - Retorna uma lista de todos os registros de histórico de traduções em formato JSON.

### Administração

- `DELETE /admin/history/<id>` - Exclui um registro de histórico específico. Requer um token de autorização no cabeçalho da requisição.

## Uso

### Inteface Web

- Acesse a interface do projeto em seu navegador:

- URL: http://127.0.0.1:8000
- Realize traduções de texto entre diferentes idiomas de forma intuitiva.

### API Endpoints

#### Listagem de Histórico

Envie uma requisição GET para `http://127.0.0.1:8000/history` para obter todos os registros de tradução.

#### Exclusão de Histórico

Envie uma requisição DELETE para `http://127.0.0.1:8000/admin/history/<id>` com o cabeçalho `Authorization` contendo o token do administrador e o cabeçalho `User` com o nome de usuário do administrador.

## Licença

Este projeto é licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

