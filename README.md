# Tutor Scheduler

A Django web app for scheduling peer tutor sessions in Boarding School's Academic Resource Center

<!-- [![Django CI](https://github.com/tylertaewook/tutor-scheduler-django/actions/workflows/ci.yml/badge.svg)](https://github.com/tylertaewook/tutor-scheduler-django/actions/workflows/ci.yml) -->
[![codecov](https://codecov.io/gh/tylertaewook/tutor-scheduler-django/branch/main/graph/badge.svg?token=KJUJHJTKVW)](https://codecov.io/gh/tylertaewook/tutor-scheduler-django)
<a href="https://github.com/tylertaewook/tutor-scheduler-django/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/tylertaewook/tutor-scheduler-django"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

[![Total alerts](https://img.shields.io/lgtm/alerts/g/tylertaewook/tutor-scheduler-django.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tylertaewook/tutor-scheduler-django/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/tylertaewook/tutor-scheduler-django.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tylertaewook/tutor-scheduler-django/context:python)

![UI](https://i.imgur.com/lXDvSMS.png)

### Features:
- User Authentication: custom user model w/ Email verification
- Tutor Session **CRUD** (Create, Read, Update, Delete): Students can sign up, edit, or delete tutor sessions. Tutors can keep track of upcoming sessions. Teachers have access to admin panel and can refer students to sessions
- Profile pages with upcoming and past sessions depending on user groups; Students and tutors can view past and upcoming tutor sessions.
- Testing: **pytest + codecov + Factoryboy**
- Depolyed using **docker-compose and heroku**


### Dev Roadmap
You can track my dev progress HERE!

(***Update: all tasks finished!!***)

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b3d1dcef-0c92-48f3-95c0-fb6de80cf143/Screen_Shot_2022-01-04_at_4.28.40_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220104T072854Z&X-Amz-Expires=86400&X-Amz-Signature=76d627802ba013cdc696e0bee64bc6a6367c2ea62b8deb31983e5d135e0b8559&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Screen%2520Shot%25202022-01-04%2520at%25204.28.40%2520PM.png%22&x-id=GetObject)


### [Getting Up and Running Locally](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)

### [Getting Up and Running Locally With Docker](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
