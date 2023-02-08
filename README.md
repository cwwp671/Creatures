# Creatures

An application for uploading and managing creatures for an imagined video game.

This application is built using `django`, `django-rest-framework`, and utilizes django's built-in session authentication.

## Running Creatures

Creatures is dockerized and can be easily built and started with one command:

```
docker-compose up -d
```

Tests can be run with the command:

```
docker-compose exec web python manage.py test creatures
```

Stop and delete:
```
docker-compose stop
docker-compose rm
```

## Interacting with Creatures

Browse to http://localhost:8000/api/creatures/

A default user has been configured for interaction with the browsable API:
- Username: `Default_User`
- Password: `default1234`
