# Database Benchmarks

# Table of Contents
1. [Overview](#overview)
2. [Disclaimer](#disclaimer)
3. [CQRS principals](#cqrs-principals)

# Overview
Purpose of this project is to benchmark many databases for the same commands.
In order to do that, we will use:

- docker - for quick and simple database managment
- python + pytest - we need to choose one simple benchmark tool. We just choose Python. pytest is very efficent in implementing tests
- CQRS - this approach will help as to make the same result for different databases.

# Disclaimer

This repo does not aims to be "the best database benchmark there is". Doing so would be very hard, because we would need to make queries in the database's language whis is much more work.
We will use Python's libraries to connect to different databases and use it only in the Query and Command objects. This will give us the possibility to use the same tests for every database. So this is more like "database bindings benchmark" rather "database benchmark". But lets be honest: in python projects we would like to use python's bindings rather then use raw database language. And we would like to know "how good THIS binding will work with THIS database".
The next big purpose of this project is to train ourselfs in the CQRS metodology, so we will know how to implement this in new projects.

# CQRS principals

What is CQRS is described here: https://martinfowler.com/bliki/CQRS.html
The simples way to describe it is this: to separate database action from the logic of the rest of the application. Saing this is not enough, so we need to follow this rules:
- mock Query and Command objects in the app's tests. This way we will separate the app's logic from the Query and Command implementation.
  This principal is not used in this project, because we will do only Query and Command tests.
- Make only black-box tests for Query and Command objects. This mean, if you want to check if your Command nad Query is working properly, then use only these objects. Do not, for example, make saves to the database in other places then Command. Do not check what is in the database in other places then Query. This makes these tests independent on the database itself. So you can implement Query and Command objects for other databases and use the same tests for it.
- Make 2 kind of models: normal Models (used in app) and Data Models where needed (to use in Query and Command). Different ORMs use different Model systems, but in the app we need to use one unified model which will be returned by the Query and Command objects.
