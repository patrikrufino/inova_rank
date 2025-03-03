## Instalação e uso local

Projeto desenvolido em`Python 3.13` com `poetry 1.8.2`.

Para reproduzir o projeto, deve-se:

1. Clonar o repositório.

2. Criar arquivo `.env` com as seguintes variáveis:

- `DATABASE_URL`: URL de conexão com o banco de dados
- `SECRET_KEY`: chave secreta para proteger token de autenticação
- `ALGORITHM`: algorítimo para encriptografar o token.
- `ACCESS_TOKEN_EXPIRE_MINUTES`: tempo de expiração do token JWT em minutos.

    Exemplo:
    ```env
    DATABASE_URL="sqlite:///database.db"
    SECRET_KEY="Sua chave aqui"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

3. É possível executar o projeto em:

- Diretamente em seu computador, executando:

    ```sh
    poetry install
    poetry run task run
    ```

4. Acesse a aplicação no navegador:

    ```sh
    http://localhost:8000