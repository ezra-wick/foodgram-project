# Foodgram


![foodgram-project](https://github.com/ezra-wick/foodgram-project/workflows/Foodgram/badge.svg)


### Description
Foodgram is a site that lets you create your own recipes and share them with other people. You can also subscribe to recipe authors and add recipes to your shop-list - 
and download the list with all ingredients you need.

The site is available on http://84.252.137.96


## Tech stack
- Python 3.9
- Django and Django Rest Framework
- PostgreSQL
- Gunicorn + Nginx
- CI/CD: Docker, docker-compose, GitHub Actions
- Yandex.Cloud

## Setup
- Clone the github repository
    ```
    git clone https://github.com/ezra-wick/foodgram-project.git
    ```
- Enter the project directory
    ```
    cd foodgram-project/
    ```
- Start docker-compose
    ```
    docker-compose -f docker-compose.yaml up -d
    ```
- Create superuser
    ```
    docker-compose -f docker-compose.yaml run --rm web python manage.py createsuperuser
    ```
### Optional
- Load test data
    ```
    docker-compose -f docker-compose.yaml run --rm web python manage.py loaddata fixtures.json
    ```
- Load ingredients
    ```
    docker-compose -f docker-compose.yaml run --rm web python manage.py enter_data
    ```
