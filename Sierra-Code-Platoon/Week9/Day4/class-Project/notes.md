
# Full Stack App Day-4

## good commands
- python3 manage.py showmigrations {AppFolder}
- (on the front-end directory) after adding this code in package.json under line 8
    - "build:watch": "vite build --watch",
    - type this command in terminal "npm run build:watch"
    - make sure to move the resources like img in asset folder in src directory


## Implementation / Construction Steps

TODO:

- Django config
    - [x] add django rest framework to installed apps
    - [X] create django app
        - [X] add to settings.py
        - [X] set up the urls route
        - [X] wait and jump to setup the database
- [X] Setup Postgresql (setup database) 
    - [X] create database
    - [X] set db to postgres in settings.py
    - [X] set name of db in settings.py
    
- [X] setup user auth model
    - [X] create custom user model from abstract base user
        - example: AUTH_USER_MODEL = 'AppFolderName.AppUser'
    - [X] in settings.py specify user model name
    - [X] python3 manege.py makemigrate, to test this  

- [X] setup our static file directory
    - [X] create static dir
    - [X] set static dir path in settings.py

- [X] Config vite to build react app (client) for django
    - [X] set build output directory
    