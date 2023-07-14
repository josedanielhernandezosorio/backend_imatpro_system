# Intelligent Mathematical Problem Solving System (ImatPRO)

[![Django CI](https://github.com/josedanielhernandezosorio/backend_imatpro_system/actions/workflows/django.yml/badge.svg?branch=develop)](https://github.com/josedanielhernandezosorio/backend_imatpro_system/actions/workflows/django.yml)

## Información General de la Contruccion 🛠️

> La tecnologias con las que se contruyo el backend

| Nombre     |   Versión    |        Tipo         |
|------------|:------------:|:-------------------:|
| Python     |              |      Lenguaje       |
| Django     |              |      Framework      |
| Docker     |   19.03.4    |    Contenedores     |
| PostgreSQL |     11.5     |    Base de datos    |
| Mongo      |              | Base de datos NOSQL |
| MacOS      |    10.15     |  Sistema Operativo  |
| Linux      | Ubuntu 19.10 |  Sistema Operativo  |

## Creacion de Base de Datos, para pruebas.

docker exec -it <container_name> bash

psql -U postgres

create user <my-user> ;

alter user <my-user> with password '<my-user-password>';

create database <my-database>;

GRANT ALL PRIVILEGES ON DATABASE <my-database> TO <my-user>;

#### Autores

| Nombre                           |                     Email                     |          Rol          |
|----------------------------------|:---------------------------------------------:|:---------------------:|
| [José Daniel Hernández Osorio]() | josedaniel.hernandez.osorio@sofyntelligen.com | FullStack Development |

##### Fecha del documento

> 23-09-2022

##### Tecnologías relacionadas

> `Python` `Django` `Docker` `Mongo` `PostgreSQL` `Native Application`
