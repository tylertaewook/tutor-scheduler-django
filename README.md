# tutor-scheduler-django
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![Issues](https://img.shields.io/github/issues-raw/tterb/PlayMusic.svg?maxAge=25000)](https://github.com/tylertaewook/tutor-scheduler-django/issues)  

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
