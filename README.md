# KBE

![Architekturdiagram](diagrams/LappenShop.png)
clone this repository and run
```
$ docker-compose up
```
This starts up a cluster of:
 1. products (the main app that offers all the products inkl. gif and tax),
 2. db (a postgres db linked direktly to products service)
 3. tax-calculator (a service to calculate 19% tax to a given amount in cents), 
 4. products-csv-exporter,
 5. products-csv-importer, 
 6. Mangodb1
 7. Mangodb2

in order to look into one of your running docker-containers run
```
$ docker-compose exec <the name of your container> bash
```
(I changed this to
```
$ hexhex <the name of your container> bash
```
on my machine and can highly recommend)

once you hexed a shell in: 
 1. products,
 2. tax-calculator, 
 3. products-csv-exporter,
 4. products-csv-importer, 

you can activate the virtual env by running: 
```
$ source `poetry env info --path`/bin/activate
```
and, e.g. create a superuser for products, so that you can also PUT new products into db
```
$ python manage.py createsuperuser
```
your trusty endpoints would be: 
1. Product_Service = http://localhost:8000/products/ -> productssuperuser=admin password=passwort123
2. Swagger documentation of Products_Service API = http://localhost:8000/swagger/#/
3. Tax_Calculation_Service = http://localhost:8001/mwst/?cent=100

![Sequenzdiagram](diagrams/LappenSequenz.png)

1. mkdir 'myfunnyproject'
2. poetry init
3. skip through creating pyproject.toml creation
4. poetry add django
5. django-admin startproject 'myfunnyprojectapp
6. cd 'myfunnyprojectapp'
7. poetry run python manage.py runserver starts the server -> visit localhost:8000 to check if install was successfull
   (from: https://rasulkireev.com/managing-django-with-poetry/)
    btw. If you need to have the requirements.txt file with all the dependencies, 
   you can run poetry export -f requirements.txt --output requirements.txt. 
   If you have configured a CI/CD job that auto deploys your project, you can add 
   this function as a step, which will generate the updated version on each update.
o inlcude restframework https://www.django-rest-framework.org/tutorial/quickstart/ i included a super user psswd passwort123

