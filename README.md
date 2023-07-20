# Intelligent Mathematical Problem Solving System (ImatPRO)

[![Django CI](https://github.com/josedanielhernandezosorio/backend_imatpro_system/actions/workflows/django.yml/badge.svg?branch=develop)](https://github.com/josedanielhernandezosorio/backend_imatpro_system/actions/workflows/django.yml)

## Installation 🛠️

> La tecnologias con las que se contruyo el backend

| Nombre     |   Versión    |        Tipo         |
|------------|:------------:|:-------------------:|
| Python     |     3.9      |      Lenguaje       |
| Pip        |    23.1.2    |      Libreria       |
| Django     |     3.2      |      Framework      |
| Docker     |   19.03.4    |    Contenedores     |
| PostgreSQL |     11.5     |    Base de datos    |
| Mongo      |              | Base de datos NOSQL |
| MacOS      |    10.15     |  Sistema Operativo  |
| Linux      | Ubuntu 19.10 |  Sistema Operativo  |

## Installation

Se debera confirmar que se cuente con las herramientas antes mensionadas, para poder creara el ambiente  virtual del proyecto y asi como instalacion de las dependencias de los pip´s

```bash
 $ python -m venv virtual-backend-imatpro-system
 $ source virtual-backend-imatpro-system/bin/activate
 (virtual-backend-imatpro-system) $
```

Se realizara en seguida las intalacion de las dependencias:

```bash
 (virtual-backend-imatpro-system) $ pip install --upgrade pip
 (virtual-backend-imatpro-system) $ pip install -r requirements.txt
```


## Run Locally



```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

## Deployment

To run tests, run the following command

```bash
 $ docker compose down
 $ docker system prune -a
 $ docker compose up -d --force-recreate --build
```

## Running Tests

To run tests, run the following command

```bash
 $ python manager.py test
```

### Creacion de Base de Datos, para pruebas.

```bash
docker-compose rm -f && docker-compose stop -t 1 && docker-compose down && docker system prune -af --volumes && docker-compose down
 $ docker-compose rm -f
 $ docker-compose stop -t 1
 $ docker-compose down
 $ docker system prune -af --volumes
 $ docker-compose down
 $ docker compose up -d --force-recreate --build
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG`

`SECRET_KEY`

`DJANGO_ALLOWED_HOSTS`

`POSTGRESQL_NAME`

`POSTGRESQL_USER`

`POSTGRESQL_PASS`

`POSTGRESQL_HOST`

`POSTGRESQL_PORT`

`ANOTHER_API_KEY`

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

## Authors

| Name                                                                         |                     Email                     |            Rol             |
|------------------------------------------------------------------------------|:---------------------------------------------:|:--------------------------:|
| [José Daniel Hernández Osorio](https://github.com/josedanielhernandezosorio) | josedaniel.hernandez.osorio@sofyntelligen.com | Cloud Software Development |



## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

## Feedback

If you have any feedback, please reach out to us at fake@fake.com

## 🛠 Skills
Javascript, HTML, CSS...

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://www.linkedin.com/in/josedanielhernandezosorio/)](https://www.linkedin.com/)

##### Fecha del documento

> 23-09-2022****







asgiref==3.6.0
attrs==22.2.0
bcrypt==4.0.1
certifi==2022.12.7
cffi==1.15.1
charset-normalizer==3.1.0
cryptography==40.0.1
distro==1.8.0
docker==6.0.1
docker-compose==1.29.2
dockerpty==0.4.1
docopt==0.6.2
idna==3.4
jsonschema==3.2.0
lark-parser==0.12.0
lxml==4.9.2
Markdown==3.3.4
packaging==23.0
paramiko==3.1.0
pycparser==2.21
PyNaCl==1.5.0
pyrsistent==0.19.3
python-dotenv==0.21.1
pytz==2023.2
PyYAML==5.4.1
requests==2.28.2
six==1.16.0
sqlparse==0.4.3
texttable==1.6.7
urllib3==1.26.15
websocket-client==0.59.0

