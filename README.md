# Tutor Scheduler

A Django web app for scheduling tutor sessions in Kent School's Academic Resource Center(ARC)

[![Django CI](https://github.com/tylertaewook/tutor-scheduler-django/actions/workflows/ci.yml/badge.svg)](https://github.com/tylertaewook/tutor-scheduler-django/actions/workflows/ci.yml)
<a href="https://github.com/tylertaewook/tutor-scheduler-django/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/tylertaewook/tutor-scheduler-django"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

[![Total alerts](https://img.shields.io/lgtm/alerts/g/tylertaewook/tutor-scheduler-django.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tylertaewook/tutor-scheduler-django/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/tylertaewook/tutor-scheduler-django.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tylertaewook/tutor-scheduler-django/context:python)

License: MIT

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0ea6468a-5d30-4f81-b5d1-6caf16768a36/Screen_Shot_2022-01-12_at_11.02.43_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220112T140305Z&X-Amz-Expires=86400&X-Amz-Signature=e052c3ceebe22ae04929ee5fbba4f3418835107820346be1f6ad04116c9ef60c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Screen%2520Shot%25202022-01-12%2520at%252011.02.43%2520PM.png%22&x-id=GetObject)

### Dev Roadmap
You can track my dev progress [HERE](https://tylertaewook.notion.site/9e2a8e4711124483ab5d502b6a5d5880?v=e15a4d94a56640069d47edbe33319070)

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b3d1dcef-0c92-48f3-95c0-fb6de80cf143/Screen_Shot_2022-01-04_at_4.28.40_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220104T072854Z&X-Amz-Expires=86400&X-Amz-Signature=76d627802ba013cdc696e0bee64bc6a6367c2ea62b8deb31983e5d135e0b8559&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Screen%2520Shot%25202022-01-04%2520at%25204.28.40%2520PM.png%22&x-id=GetObject)


## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy tutor_scheduler

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
