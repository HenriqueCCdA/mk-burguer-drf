# mk-burguer-drf

![Imagem](./docs/img/)

Api feita em DRF para o frontend [mk-burger](https://github.com/HenriqueCCdA/mk-burger-front)

| :placard: Vitrine.Dev |     |
| -------------         | --- |
| :sparkles: Nome       | `Make Burger API`
| :label: Tecnologias   | `Django Rest Framework`, `Python`, `Postgres`, `Pytest`, `Docker`, `Poetry`, `Ruff`, `codecov`, `swagger`
| :rocket: URL          |

## Desenvolvimento local

Instalando dependencias com o `poetry`

```bash
poetry install
```

Formatador com `Black`

```bash
task fmt
```

Linter com `Ruff`

```bash
task linter
```

Rodando os testes

```bash
task tests
```

Listar todos os comandos do `taskipy`

```bash
task -l
```

Variaveis de ambiente com `python-decouple`

```bash
SECRET_KEY="Sua chave secreta aqui"

DEBUG=True
DOC_API=True

ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=postgres://test_user:test_password@localhost:5432/test_user
```

Para usar o `sqlite` basta retirar a variável `DATABASE_URL`

Subindo o banco de dados `Postgres` com docker-compose

```bash
docker compose database up -d
```

Instalando o pre-commit

```bash
pre-commit  install
```

## Desenvolvimento com docker

Subindo a aplicação
```bash
docker compose up
```

Rodando os testes

```bash
docker compose run backend task tests
```
