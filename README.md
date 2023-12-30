# mk-burguer-drf

![Imagem](./docs/img/swagger.png?text=imagem_do_projeto#vitrinede)

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

Subindo o banco de dados `Postgres` com `docker-compose`

```bash
docker compose database up -d
```

Instalando o pre-commit

```bash
pre-commit install
```

## Desenvolvimento com docker

Subindo a aplicação
```bash
docker compose -f docker-compose.dev.ym up
```

Rodando os testes

```bash
docker compose -f docker-compose.dev.yml run backend task tests
```

## Simulando o ambiente de produção com docker

Para simular o ambiente de produção foi usado `gunicorn` como servide de aplicação e `nginx` como servidor web.

Subindo a aplicação `nginx`, `postgres` e `gunicorn`

```bash
docker compose -f docker-compose.prod.yml up
```

Os configurações do `nginx` foram

```
server {
    listen       80;
    server_name  localhost;

    location / {
        proxy_set_header      Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://backend:8000;
    }
    location /static {
        alias /var/www/site/staticfiles;
    }
}
```

Podendo ser achas [aqui](./docker/nginx/)
