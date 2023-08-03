# Intelligent Mathematical Problem Solving System (ImatPRO)

[![Django CI](https://github.com/josedanielhernandezosorio/backend_imatpro_system/actions/workflows/django.yml/badge.svg?branch=develop)](https://github.com/josedanielhernandezosorio/backend_imatpro_system/actions/workflows/django.yml)

## Installation 🛠️

You must have the following versions of tools for installation and execution

| name       |   version    |   type    |
|------------|:------------:|:---------:|
| Python     |     3.11     | language  |
| Pip        |    23.1.2    |  library  |
| Django     |     3.2      | framework |
| Docker     |   19.03.4    | container |

When confirming that you have these startup tools, you will be able to download the preferred source code from the develop branch and then start a finish in the folder path, then we will execute the installation from terminal

Creation of virtual environment, consider that it will be created with version 3.11 of python


```bash
 ~/backend_imatpro_system] $ python -m venv virtual-backend-imatpro-system
 ~/backend_imatpro_system] $ source virtual-backend-imatpro-system/bin/activate
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $
```

installation of dependencies, these dependencies can be consulted from the file [requirements.txt](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/requirements.txt) :

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ pip install --upgrade pip
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ pip install -r requirements.txt
```

This point is optional if we do not have the updated data of the script for creating the database model

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ python manage.py makemigrations
```

## Run Local

For its execution in local there are 2 ways, one of them is having a temporary base of sqlite type and having a postgresql database from a container with docker

### Local with sqlite 

It must be considered that in this execution the following environment variables are being [used](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/config/app/.env.config.app), which are by default

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ python manage.py migrate
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ python manage.py runserver
```

Everything should be executed correctly and postman can be used with the local environment which is found in the documentation section attached [link](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/doc/ImatPro.postman_collection.json).

### Local with docker postgresql

The construction of the postgresql container will start with the following commands

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ cd docker/local/postgresql
 (virtual-backend-imatpro-system) ~/backend_imatpro_system/docker/local/postgresql] $ docker compose up --build
 
 .
 .
 .
 
 imatpro_postgres_local  | 2000-00-00 00:00:00.000 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
 imatpro_postgres_local  | 2000-00-00 00:00:00.000 UTC [1] LOG:  listening on IPv6 address "::", port 5432
 imatpro_postgres_local  | 2000-00-00 00:00:00.000 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
 imatpro_postgres_local  | 2000-00-00 00:00:00.000 UTC [46] LOG:  database system was shut down at 2000-00-00 00:00:00 000
 imatpro_postgres_local  | 2000-00-00 00:00:00.000 UTC [1] LOG:  database system is ready to accept connections
```

Once finished building the container, in another finish the project will start. It must be considered that in this execution the environment variables of the local configuration file are being used, [it is attached](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/config/app/.env.config.app.local)

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ python manage.py migrate --settings=settings.local
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ python manage.py runserver --settings=settings.local
```

Everything should be executed correctly and postman can be used with the docker environment which is found in the documentation section attached [link](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/doc/ImatPro.postman_collection.json).

> note: for any execution you can launch the [status](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/doc/ImatPro.postman_collection.json) architecture service o si es el caso: `http://127.0.0.1:1234/imatpro/api/v1.0.0/mathematical/state/`

## Running Tests

For the execution of the unit tests and thus validate that there are no impacts on future changes in the APIs, the following command can be executed

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ python manage.py test 
```

## Deployment

For the deploy, currently there is only one local, which is done through docker in a local, just executing the following statements:

```bash
 (virtual-backend-imatpro-system) ~/backend_imatpro_system] $ cd docker/work/
 (virtual-backend-imatpro-system) ~/backend_imatpro_system/docker/work/] $ docker compose up --build
 
 .
 .
 .
 
 imatpro_backend_work        | [2000-00-00 00:00:00 +0000] [1] [INFO] Starting gunicorn 21.2.0
 imatpro_backend_work        | [2000-00-00 00:00:00 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
 imatpro_backend_work        | [2000-00-00 00:00:00 +0000] [1] [INFO] Using worker: sync
 imatpro_backend_work        | [2000-00-00 00:00:00 +0000] [9] [INFO] Booting worker with pid: 9
 imatpro_backend_work        | [2000-00-00 00:00:00 +0000] [10] [INFO] Booting worker with pid: 10
 imatpro_backend_work        | [2000-00-00 00:00:00 +0000] [11] [INFO] Booting worker with pid: 11
```

Everything should be executed correctly and postman can be used with the local environment which is found in the documentation section attached [link](https://github.com/josedanielhernandezosorio/backend_imatpro_system/blob/develop/doc/ImatPro.postman_collection.json).


### Creacion de Base de Datos, para pruebas.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file, configurable by environment

```
DEBUG
SECRET_KEY
DJANGO_ALLOWED_HOSTS
POSTGRESQL_NAME
POSTGRESQL_USER
POSTGRESQL_PASS
POSTGRESQL_HOST
POSTGRESQL_PORT
ANOTHER_API_KEY
```


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


## Tech Stack

**Client:** React, Next.js, TailwindCSS

**Server:** Django, Django Rest Framework

## Feedback

If you have any feedback, please reach out to us at fake@fake.com

## Authors

| Name                                                                         |                     Email                     |            Rol             |
|------------------------------------------------------------------------------|:---------------------------------------------:|:--------------------------:|
| [José Daniel Hernández Osorio](https://github.com/josedanielhernandezosorio) | josedaniel.hernandez.osorio@sofyntelligen.com | Cloud Software Development |

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://www.linkedin.com/in/josedanielhernandezosorio/)](https://www.linkedin.com/)
