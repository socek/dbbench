# Database Benchmarks

# Table of Contents
1. [Overview](#overview)
2. [Disclaimer](#disclaimer)
3. [CQRS principals](#cqrs-principals)

# Overview
Purpose of this project is to benchmark databases using set of same commands.
In order to do that, we will use:

- docker - for quick and simple database management
- python + pytest - we need to choose one simple benchmark tool. We just choose Python. pytest is very efficient in implementing tests
- CQRS - this approach will help us sharing commands between databases tests.

# Disclaimer

This repo does not aim to be "the best database benchmark there is". Doing so would be very hard, because we would need to make queries in the database's language which is much more work.
We will use Python's libraries to connect to different databases and use it only in the Query and Command objects. This will give us the possibility to use the same tests for every database. So this is more like "database bindings benchmark" rather than "database benchmark". But lets be honest: in python projects we would like to use python's bindings rather then use raw database language. And we would like to know "how good THIS binding will work with THIS database".
The other goal of this project is to train ourselves in the CQRS methodology, so we will know how to implement this in new projects.

We are using docker in this project. Please be aware that this may be a factor as well, because docker use overlay2 for filesystem in the containers. In production, the database may be have different speed on different filesystems.

# CQRS principals

CQRS is described here: https://martinfowler.com/bliki/CQRS.html
The simplest way to describe it: separation of database actions from the logic of the rest of the application. In order to achive that we will follow this rules:
- mock Query and Command objects in the app's tests. This way we will separate the app's logic from the Query and Command implementation.
  This principal is not used in this project, because we will do only Query and Command tests.
- Make only black-box tests for Query and Command objects. This means, if you want to check if your Command and Query is working properly, then use only these objects. Do not, for example, alter database state in other places then Command. Do not check what is in the database in other places then Query. This makes these tests independent from the database itself. So you can implement Query and Command objects for other databases and use the same tests for it.
- Make 2 kind of models: normal Models (used in app) and Data Models where needed (to use in Query and Command). Different ORMs use different Model systems, but in the app we need to use one unified model which will be returned by the Query and Command objects.

# How to use this

Simply, just run pytest.

```
docker-compose run --rm backend pytest
```

This will start all of the tests, but this is not what we want. We want to check speed of only 1 database, so we will use the pytest.mark functionality:

```
docker-compose run --rm backend pytest -m postgresql
```

You should read the time it took from the pytest log. I know, that this is pretty weak, but I will make it more usable in the future.

All supported markers are:

* postgresql
* sqlite3
* sqlite3memory: sqlite3 when the database file is in tmpfs
* mysql
* mongodb

