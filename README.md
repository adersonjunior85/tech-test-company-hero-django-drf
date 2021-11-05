# Teste Python - Company Hero

### Criar uma API REST com Django e Rest Framework onde consiga acessar organizações e seus funcionários.
#
#
# Utilização da API:



### GET /companies/
#
##### Retorna todas as empresas cadastradas
#
##### Exemplo de resultado:
#
#
```bash
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "nome": "Amazon.com",
        "cnpj": "15436940000103",
        "site": "https://www.amazon.com.br",
        "email": "amazon@amazon.com",
        "endereco": "Seattle",
        "telefone": "88888888888"
    },
    {
        "id": 2,
        "nome": "Company Hero",
        "cnpj": "20240272000176",
        "site": "www.companyhero.com",
        "email": "companyhero@companyhero.com",
        "endereco": "Av. Paulista, 171 - 4º andar - Bela Vista, São Paulo - SP, 01311-000",
        "telefone": "11999999999"
    }
]
```
### GET /companies/<id>
#
##### Retorna a empresa com o seu respectivo ID
#
##### Exemplo de resultado:
#
```bash
{
    "id": 1,
    "nome": "Company Hero",
    "cnpj": "20240272000176",
    "site": "https://www.companyhero.com",
    "email": "companyhero@companyhero.com",
    "endereco": "Av. Paulista, 171 - 4º andar - Bela Vista, São Paulo - SP, 01311-000",
    "telefone": "11999999999"
}
```
### POST /companies/
#
##### Faz o POST de uma empresa
#
##### Exemplo de post:
#
#
```bash
{
    "nome": "Company Hero",
    "cnpj": "20240272000176",
    "site": "www.companyhero.com",
    "email": "companyhero@companyhero.com",
    "endereco": "Av. Paulista, 171 - 4º andar - Bela Vista, São Paulo - SP, 01311-000",
    "telefone": "11999999999"
}
```
### GET /employees/
#
##### Retorna todos os funcionários
#
##### Exemplo de resultado:
#
```bash
{
    "id": 5,
    "name": "Robson Nunes",
    "cargo": "Web Design",
    "cpf": "72225655144",
    "companies": [
        {
            "id": 1,
            "nome": "Amazon.com",
            "cnpj": "15436940000103",
            "site": "https://www.amazon.com.br",
            "email": "amazon@amazon.com",
            "endereco": "Seattle",
            "telefone": "88888888888"
        },
        {
            "id": 2,
            "nome": "Company Hero",
            "cnpj": "20240272000176",
            "site": "www.companyhero.com",
            "email": "companyhero@companyhero.com",
            "endereco": "Av. Paulista, 171 - 4º andar - Bela Vista, São Paulo - SP, 01311-000",
            "telefone": "11999999999"
        }
    ]
}
```
### GET /employees/<nome>
#
##### Retorna os dados do funcionário cadastrado de acordo com o nome
#
##### Exemplo de resultado:
#
```bash
{
    "id": 4,
    "name": "Marcos Vinicius",
    "cargo": "Web Developer",
    "cpf": "70025632144",
    "companies": [
        {
            "id": 1,
            "nome": "Amazon.com",
            "cnpj": "15436940000103",
            "site": "https://www.amazon.com.br",
            "email": "amazon@amazon.com",
            "endereco": "Seattle",
            "telefone": "88888888888"
        }
    ]
}
```
### POST /employees/
#
##### Executa um POST para cadastrar um funcionário
#
##### Exemplo de post:
#
```bash
{
    "name": "Robson Nunes",
    "cargo": "Web Design",
    "cpf": "72225655144"
}
```
### GET /employees/<name>/companies
#
##### Retorna exclusivamente todas as empresas do funcionário de acordo com o nome
#
##### Exemplo de resultado:
#
```bash
[
    {
        "id": 1,
        "nome": "Amazon.com",
        "cnpj": "15436940000103",
        "site": "https://www.amazon.com.br",
        "email": "amazon@amazon.com",
        "endereco": "Seattle",
        "telefone": "88888888888"
    },
    {
        "id": 2,
        "nome": "Company Hero",
        "cnpj": "20240272000176",
        "site": "www.companyhero.com",
        "email": "companyhero@companyhero.com",
        "endereco": "Av. Paulista, 171 - 4º andar - Bela Vista, São Paulo - SP, 01311-000",
        "telefone": "11999999999"
    }
]
```
### POST /employees/<name>/companies
#
##### Cadastra a empresa para o funcionario <name> enviando o id
#
##### Exemplo de post:
#
```bash
{
    "companies": 1
}
```
# Explicação da lógica utilizada e decisões tomadas durante o projeto
##### O projeto teve uma dinâmica bem interessante, e eu quis aproveitar pra explorar algumas funcionalidades que eu não tinha trabalhado antes aproveitando o intuito do projeto de usar a criatividade, que me fez forçar bastante a usar a [documentação](https://www.django-rest-framework.org) e aprender coisas novas. Foi muito divertido a experiência e me rendeu ótimos aprendizados.