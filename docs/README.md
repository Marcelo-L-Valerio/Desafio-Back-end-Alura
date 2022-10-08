# Desafio Back-end Alura v4

## Desafio proposto pela plataforma alura de desenvolvimento de uma API rest de controle financeiro

###

### Marcelo Lopes Valerio - email: mar.valerio@hotmail.com.br - Linkedin: Marcelo Lopes Valerio

## Objetivos pessoais: aprofundar o conhecimento de desenvolvimento web utilizando o Django Rest Framework como base do projeto, para consolidar as técnicas desenvolvidas e compreender melhor alguns conceitos

## Objetivos do desafio: Desenvolver uma API com as seguintes funcionalidades: 

### - CRUD de recitas e despesas, com os campos: classificação, descrição, valor e data

### - Possibilidade de filtrar as receitas e despesas pelo mês, inserindo na URL /ano/mes

### - Gerar um relatório mensal dos lançamentos, mostrando o valor total de despesas/receitas do mes, saldo final, e uma descrição detalhada das despesas e receitas de acordo com as classificações

## Outros requisitos do desafio:

### - Sistema de autenticação (login) para permissão de visualizar/alterar os dados

### - Desenvolvimento de testes automatizados

### - Validações de dados inseridos

## Regras de negocio adicionais:

### - Sem despesas duplicadas no mesmo mês

### - Filtro de receitas/despesa por dia, classificação: /?classificacao=<classificacao>&dia=<dia>

### - Ordenação de dia por crescente/decrescente: /?ordering=(+ ou -)dia

### - Filtro de receitas/despesas por descrição: /?search=<descricao>

## Funcionalidades extras para melhor aprendizado:

### - ainda em desenvolvimento

## Instruções de instalação do código:

###

### Rode os seguintes comandos para instalação dos pacotes necessarios:

    python -m venv .venv

### Obs: lembre-se de ativar o venv antes de prosseguir

    pip install -r requirements.txt

### Renomeie o arquivo exemplo.env, e preencha os dados pedidos, e crie um schema no mySQL com o nome colocado no arquivo

### A seguir, é necessário realizar a migração das tabelas dos modelos para o banco de dados:

    ./manage.py makemigrations releases
    ./manage.py migrate

### Por ultimo, crie o superuser (login) e inicie o servidor local:

    ./manage.py createsuperuser
    ./manage.py runserver

## Funcionalidades da API:

###

### Os end-points desenvolvidos foram os seguintes:

### Home - http://127.0.0.1:8000
### CRUD/list despesas - http://127.0.0.1:8000/despesas/
### CRUD/list receitas - http://127.0.0.1:8000/receitas/
###
### list despesas de um mes - http://127.0.0.1:8000/despesas/<ano>/<mes>/
### list receitas de um mes - http://127.0.0.1:8000/receitas/<ano>/<mes>/
###
### list resumo de um mes - http://127.0.0.1:8000/resumo/<ano>/<mes>/