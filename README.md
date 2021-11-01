# KBE

![gif](https://media.giphy.com/media/ZbeonvEvZBwNeWGC9V/giphy.gif)

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

