# Tweet Scrapping
 Projeto de Web Scrapping usando a API do Twitter com armazenamento em banco de dados

## Autor

Diego Giovanni de Alcântara Vieira

# Descrição

O projeto tem o objetivo coletar tweets seguindo determinadas constraints a partir da API do Twitter,
bem como armazená-los em um banco de dados do tipo (a decidir).

# Linguagens

O projeto é desenvolvido em Linguagem Python

# Frameworks

Tweepy: funções built-in de acesso à Twitter API.

# Instruções de Deploy

## Twitter API

O usuário deverá criar um projeto em [Twitter Developers](https://developer.twitter.com/). Para isso, o mesmo deverá ter uma conta no twitter.
Após o processo de habilitar o acesso de desenvolvedor e criar o projeto, o usuário deverá gerar os tokens de autenticação.
    * Consumer Keys: API Key & Secret - Referentes ao Projeto.
    * Access Tokens: Acess Token & Secret - Referentes ao Usuário.

Garanta guardar os tokens gerados em um lugar seguro. Caso necessário, o usuário pode revogar acesso e/ou criar novos tokens nas configurações no Twitter Developers.

## Fornecendo chaves ao projeto

As informações de acesso são necessárias para autenticar o Handler que dá acesso ao StreamListener do projeto. Não há persistência de dados quanto aos tokens para evitar vazamento de informações pessoais. Considerando isso, toda vez que o usuário quiser acessar o StreamListener, deverá fornecer novamente as keys, num total de 4 itens.