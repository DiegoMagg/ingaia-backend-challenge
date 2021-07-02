# inGaia Backend Challenge

[![codecov](https://codecov.io/gh/DiegoMagg/ingaia-backend-challenge/branch/main/graph/badge.svg?token=BOS8KXN47P)](https://codecov.io/gh/DiegoMagg/ingaia-backend-challenge)
[![Build Status](https://travis-ci.com/DiegoMagg/ingaia-backend-challenge.svg?branch=main)](https://travis-ci.com/DiegoMagg/ingaia-backend-challenge)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-395/)


Este repositório contêm o código em resposta ao teste técnico proposto pela inGaia.

# Requirements:

1. [Pipenv](https://pipenv.pypa.io/en/latest/)
2. [Docker](https://docs.docker.com/get-docker/)
3. [Docker Compose](https://docs.docker.com/compose/install/)


A definição dos serviços encontram-se nos arquivos docker-compose.yaml que são:

# API Consulta (API1)
1. **api-consulta** - Servidor WSGI gunicorn para aplicação.
2. **migrations** - Executa as migrações das tabelas do BD sempre que houver modificação nos arquivos de migration.
3. **fixtures** - Popula o banco de dados com exemplos para teste dos endpoints.

## Variáveis de ambiente
|       Variável        |      Exemplos      |     Definição      |
|-----------------------|--------------------|-----------|
|DJANGO_SETTINGS_MODULE |`"settings.modulo"`             |Define qual *settings* usar|
|API_VERSION            |`"v1"`                          |Define a versão da API nas urls e no Swagger|
|DJANGO_SECRET_KEY      |`"token"`                       |Token usado pelo Django  |
|ALLOWED_HOSTS          |`"exemplo.com,api-consulta` |*Hosts* separados por vírgula|
|SENTRY_DSN             |`"https:/sentry.com"`|URL para monitorar erros na aplicação *online*  (opcional)|
|API_URL                |`"https:/api-consulta.diegomagg.com.br"`|URL *root* da api (necessário para que o swagger use HTTPS nas requisições)|

# API Cotação (API2)
1. **api-cotacao** - Servidor WSGI gunicorn para aplicação.

## Variáveis de ambiente
|       Variável        |   Exemplos         |     Definição      |
|-----------------------|--------------------|-----------|
|DJANGO_SETTINGS_MODULE |`"settings.modulo"`             |Define qual *settings* usar|
|API_VERSION            |`"v1"`                          |Define a versão da API nas urls e no Swagger|
|DJANGO_SECRET_KEY      |`"token"`                       |*Token* usado pelo Django  |
|ALLOWED_HOSTS          |`"exemplo.com,api-cotacao"` |*Hosts* separados por vírgula|
|SENTRY_DSN             |`"https:/sentry.com"`|URL para monitorar erros na aplicação *online*  (opcional)|
|API_URL                |`"https:/api-cotacao.diegomagg.com.br"`|URL *root* da api (necessário para que o swagger use HTTPS nas requisições)|
|API_CONSULTA_URL|`"http://api-consulta"` |URL base onde a *view* de cotação busca as informações da **API_1**|


## Testando as APIs:



[API_1 - Consulta](https://api-consulta.diegomagg.com.br/v1) - Esta API pode ser testada a partir do swagger.
Após clicar no botão *"Try it out"*, digite `empreendimento x` no campo `nome` e clique em
executar. Uma query será executada no sqlite e o output é serializado resultando no json:


```json
{
  "nome": "empreendimento x",
  "valor_metro_quadrado": "1209.02"
}
```
via curl:

```bash
curl -X GET "https://api-consulta.diegomagg.com.br/v1/valor-metro-quadrado/empreendimento%20x"
```

O mesmo ocorre com o "empreendimento y":

```json
{
  "nome": "empreendimento y",
  "valor_metro_quadrado": "1191.84"
}
```

```bash
curl -X GET "https://api-consulta.diegomagg.com.br/v1/valor-metro-quadrado/empreendimento%20y"
```

[API_2 - Cotação](https://api-cotacao.diegomagg.com.br/v1) Esta API pode ser testada a partir do swagger.
Após clicar no botão *"Try it out"*, digite `empreendimento x` no campo `nome` e um valor numérico entre `10` e `10000`*. As informações de valor do metro quadrado será requisitado da
**API_1** e o cálculo efetuado.

```json
{
  "nome": "empreendimento x",
  "quantidade_metros_quadrados": 123,
  "total": 148709.46
}
```

*Caso a quantidade em metros quadrados seja inferior à 10, este será o output:
```json
{
  "quantidade_metros_quadrados": [
    "Certifique-se de que este valor seja maior ou igual a 10."
  ]
}
```
O mesmo se aplica caso o valor seja maior que 10000


# Rodando as aplicações local
```bash
$ git clone git@github.com:DiegoMagg/ingaia-backend-challenge.git
$ cd ingaia-backend-challenge
```

```bash
$ echo 'DJANGO_SETTINGS_MODULE="settings.test"
API_VERSION="v1"
DJANGO_SECRET_KEY="^u$2f)9(@#a591w3i+b+i0+m30d86zkcn(v)t4!j)3-)mc21o="
ALLOWED_HOSTS="localhost"
SENTRY_DSN=""
API_URL="http://localhost:9000"
' >> api_consulta/.env
```

```bash
$ echo 'DJANGO_SETTINGS_MODULE="settings.test"
API_VERSION="v1"
DJANGO_SECRET_KEY="t$%hq&oofr8g@a#332rd542bnj(h6dwx#da7+f0k)-)5-u_2=@"
ALLOWED_HOSTS="localhost"
SENTRY_DSN=""
API_URL="http://localhost:9010"
API_CONSULTA_URL="http://localhost:9000/v1"
' >> api_cotacao/.env
```
Nota: Estas secret keys foram geradas como exemplo.

Para subir os serviços:

```bash
make up
```
