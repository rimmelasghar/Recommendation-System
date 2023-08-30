# Movies Recommendation System API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## Create a .env file in the project directory.
change this file for your preference.
```sh
DEBUG=TRUE
SECRET_KEY=mysecretapikey
APP_ENVIROMENT=ENVIROMENT
VERSION=0.1.0
```

## Deployment using Docker containers

```sh
docker compose -f "docker-compose.production.yaml" up --build
docker compose -f "docker-compose.production.yaml" up
```

The application will be available at http://0.0.0.0:8000/api/docs/

https://github.com/rimmelasghar/Recommendation-System/blob/main/screenshots/status-endpoint.jpg
![screenshot-1](https://github.com/rimmelasghar/Recommendation-System/blob/main/screenshots/status-endpoint.jpg)

![screenshot-2](https://github.com/rimmelasghar/Recommendation-System/blob/main/screenshots/recommendation-endpoint.jpg)

