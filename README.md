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

1. Clone o repositório:

    ```bash
    git clone https://github.com/matheusrosa1/project-traduzo.git
    cd project-traduzo
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas Unix
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

4. [Opção A] Banco e Flask pelo Docker

    ```bash
    docker compose up translate
    ```

4. [Opção B] Banco pelo Docker, Flask localmente pelo ambiente virtual

    ```bash
    docker compose up -d mongodb

    python3 src/app.py
    ```

## Uso

1. Inicie o servidor Flask:

    ```bash
    flask run
    ```

    O servidor estará disponível em `http://localhost:8000`.

2. Acesse a aplicação no navegador em `http://localhost:8000` para usar a interface de tradução.

## Testes

1. **Configuração para Testes:**

    - O projeto inclui fixtures para configuração do ambiente de testes, utilizando `pytest`. As fixtures limpam e preparam o banco de dados antes de cada teste.

2. **Execução dos Testes:**

    - Para executar os testes automatizados, use:

      ```bash
      pytest
      ```

3. **Testes Específicos:**

    - Para verificar a funcionalidade de exclusão do histórico de traduções, o teste `test_history_delete` simula a exclusão de um registro específico e verifica se ele foi removido do banco de dados.

## Endpoints

### Rota Principal

- `GET /` - Exibe a página de tradução.
- `POST /` - Envia um texto para tradução e retorna o resultado.

### Histórico de Traduções

- `GET /history` - Retorna uma lista de todos os registros de histórico de traduções em formato JSON.

### Administração

- `DELETE /admin/history/<id>` - Exclui um registro de histórico específico. Requer um token de autorização no cabeçalho da requisição.

## Exemplo de Uso da API

### Tradução de Texto

Para traduzir um texto, envie uma requisição POST para `http://localhost:8000/` com os seguintes campos de formulário:

- `text-to-translate` - O texto que você deseja traduzir.
- `translate-from` - O idioma original do texto (ex.: "en").
- `translate-to` - O idioma para o qual deseja traduzir o texto (ex.: "pt").

### Listagem de Histórico

Envie uma requisição GET para `http://localhost:8000/history` para obter todos os registros de tradução.

### Exclusão de Histórico

Envie uma requisição DELETE para `http://localhost:8000/admin/history/<id>` com o cabeçalho `Authorization` contendo o token do administrador e o cabeçalho `User` com o nome de usuário do administrador.

## Licença

Este projeto é licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---

Projeto desenvolvido como parte de um exercício escolar para praticar o uso de Flask, MongoDB, e a integração com APIs externas.
