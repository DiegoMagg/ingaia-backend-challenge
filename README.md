# inGaia Backend Challenge

[![codecov](https://codecov.io/gh/DiegoMagg/ingaia-backend-challenge/branch/main/graph/badge.svg?token=BOS8KXN47P)](https://codecov.io/gh/DiegoMagg/ingaia-backend-challenge)
[![Build Status](https://travis-ci.com/DiegoMagg/ingaia-backend-challenge.svg?branch=main)](https://travis-ci.com/DiegoMagg/ingaia-backend-challenge)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-395/)


Este repositório contêm o código em resposta ao teste técnico proposto pela inGaia.

A definição dos containers encontra-se no arquivo docker-compose.yaml que são:

1. API - Servidor WSGI gunicorn para aplicação.
2. Migrations - Executa as migrações das tabelas do BD sempre que houver modificação nos arquivos de migration.
3. Fixtures - Popula o banco de dados com exemplos para teste dos endpoints.


## Requirements:

1. [Pipenv](https://pipenv.pypa.io/en/latest/)
2. [Docker](https://docs.docker.com/get-docker/)
3. [Docker Compose](https://docs.docker.com/compose/install/)
