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


http://127.0.0.1:1234/imatpro/api/v1.0.0/mathematical/state/


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

