# Documentação

# car management
## Dados

The fist user created on sign up will be the admin user. That user can do anything.

* Users from staff or admin can register new owners.

> only users staff can change data 

## without docker windows

you can run the project without docker by the next steps on terminal powershell:

* `python -m venv venv`: for creating environmental ambient
* `. /venv/Scripts/activate`: for active the environmental
* `pip install -r requirements.txt` : for installing the packages
* `flask run` : for running the flask project

## tests

For testing I use pytest

* `pytest --cov .`: run the tests
<!-- * `/api/topicos`: (mediante autenticação) Retorna JSON contendo:
  * `username`: (str) username temporário para acessar o broker
  * `password`: (str) password temporária para acessar o broker
  * `exp`: (long) número representando o epoch em que o username e a password expirarão
  * `topics`: (array de str) rotas que a aplicação deverá se inscrever para receber os dados (ver no tópico seguinte)
* `/api/administrativo`: (mediante autenticacao de usuário com privilégio administrativo): CRUD de usuários, centrais, áreas e perfis; -->


<!-- ### Fluxograma para obtenção do JSON `/topicos`

* Para cada central acessível ao usuário,adicionar ao array de tópicos a entrada: `/[nome da central]/[id da area nessa central]/+`
* Criaçao de uma entrada (allow, ipaddr, username, clientid, access, topic) na base de dados de acl para cada tópico do array [ver documentação](https://www.emqx.io/docs/en/v4.3/advanced/acl-postgres.html)
* Criação de uma entrada (username, password, salt, exp) na tabela de autenticação do emqx [ver documentação](https://www.emqx.io/docs/en/v4.3/advanced/auth-postgresql.html#postgresql-connection-information).
* Criação de uma entraada 

### Fluxograma de expiração dos pares user/password

* Verificar, a cada segundo, se há acls que devem ser removidas da base de dados de auth e de acl -->

<!-- ## CRUD de centrais

* Ao criar uma central, é necessário criar uma entrada na tabela de autenticação na tabela de autenticação do emqx [ver documentação](https://www.emqx.io/docs/en/v4.3/advanced/auth-postgresql.html#postgresql-connection-information), sem data de expiração;
* É necessário, ao criar uma central, criar uma entrada correspondente na tabela de acl para o tópico `/[nome da central]/+` (allow, ipaddr, username, clientid, access, topic) na base de dados de acl para cada tópico do array [ver documentação](https://www.emqx.io/docs/en/v4.3/advanced/acl-postgres.html) -->
