# tutor-scheduler-django
<!-- <a href="https://github.com/tyletaewook/tutor-scheduler-django/actions"><img alt="Actions Status" src="https://github.com/tylertaewook/tutor-scheduler-django/workflows/Test/badge.svg"></a> -->
[![Django CI](https://github.com/tylertaewook/tutor-scheduler-django/actions/workflows/django.yml/badge.svg)](https://github.com/tylertaewook/tutor-scheduler-django/actions/workflows/django.yml)
<a href="https://github.com/tylertaewook/tutor-scheduler-django/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/tylertaewook/tutor-scheduler-django"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

<<<<<<< Updated upstream
[![Total alerts](https://img.shields.io/lgtm/alerts/g/tylertaewook/tutor-scheduler-django.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tylertaewook/tutor-scheduler-django/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/tylertaewook/tutor-scheduler-django.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tylertaewook/tutor-scheduler-django/context:python)


A Django web app for scheduling peer tutor sessions in Kent School's Academic Resource Center; WIP



### Dev Roadmap
You can track my dev progress [HERE](https://tylertaewook.notion.site/9e2a8e4711124483ab5d502b6a5d5880?v=e15a4d94a56640069d47edbe33319070) 

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b3d1dcef-0c92-48f3-95c0-fb6de80cf143/Screen_Shot_2022-01-04_at_4.28.40_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220104T072854Z&X-Amz-Expires=86400&X-Amz-Signature=76d627802ba013cdc696e0bee64bc6a6367c2ea62b8deb31983e5d135e0b8559&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Screen%2520Shot%25202022-01-04%2520at%25204.28.40%2520PM.png%22&x-id=GetObject)

### conda env setup

```
$ cd tutorscheduler
$ conda create --name <env_name> --file conda-req.txt
```

### activate

`$ conda activate <env_name>`

### run dev server
```
$ cd tutorscheduler
$ python manage.py runserver  
```
=======
> A web app for scheduling sessions in Kent School's Academic Resource Center - Features:



 


- UI Kit: **Star Admin 2** (Free Version) by **[BootstrapDash](https://bit.ly/2UTgih5)**


- Persistance: SQLite, MySql, PostgreSQL
- Modular design, clean codebase
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Links

 

 
 

- [Star Admin Django](https://appseed.us/admin-dashboards/django-star-admin) - product page
- [Star Admin Django](https://django-star-admin.appseed-srv1.com/) - LIVE deployment
 

<br />

## Quick Start in [Docker](https://www.docker.com/)

> Change the directory inside the source code.

```bash
$ cd <GENERATED_CODE>
```

> Start the app in Docker

```bash
$ docker-compose up --build  
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

 

 
 

![Django Star Admin - Seed provided by AppSeed.](https://user-images.githubusercontent.com/51070104/142849749-130c06e2-9ebc-4c48-84c7-d35fe1ae26b3.gif)
 

<br />

## How to use it

Change the directory inside the source code.

<br />

> **Create a virtual environment** 

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Install Depenedencies**

```bash
$ # Install modules
$ pip3 install -r requirements.txt
```

<br />


> **Set up Database**

Create a new database using credentials: 

- Database Name: `tutor_django`
- Database User: `tutor_user`
- Password: to match the value saved in `core/settings.py` -> `DATABASES` section

Make sure the user has full privileges (read, write, create tables).

<br />


> **Migrate Database** (create tables)

```bash
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> **Step #4** - Start the project

```bash
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in the browser: http://127.0.0.1:8000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

<br />

---
Tutor Scheduler - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
>>>>>>> Stashed changes
