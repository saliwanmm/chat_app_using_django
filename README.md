# Login system in Python Django 

## Description

**This project is under development and will be completed soon**

## Technologies used in the project
- Python
- Django
- Postgresql
- Docker
- Docker-compose
- Git

## Local setup

**Create python environment**

```
$ python3 -m venv venv
```

**Activate python environment**

```
$ source venv/bin/activate
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Create .env file and insert there all code from .envexample file**

```
$ touch .env
```

**Build web and database containers**

```
$ sudo docker-compose build
```

**Run web and database containers**

```
$ sudo docker-compose up
```

**Superuser: username - admin, password - admin.**