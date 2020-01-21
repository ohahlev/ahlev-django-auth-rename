# DJANGO AUTH RENAME APPLICATION
![pypi](https://img.shields.io/pypi/v/ahlev-django-auth-rename) ![status](https://img.shields.io/pypi/status/ahlev-django-auth-rename)

This django application is used to rename the application label of [django.contrib.auth](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/) from
```
Authentication And Authorization
```
to
```
User Management
```

## prerequisites
The instructions below assume that you have a django project already set up; and a python virtual environment already installed and activated. 

## install from this repository
### clone
```
git clone https://github.com/ohahlev/ahlev-django-auth-rename.git
```

### go to directory ahlev-django-auth-rename
```
cd ahlev-django-auth-rename
```

### create installer package
```
make package
```

### install package
Let's say ahlev-django-auth-rename directory is in the same level as the project directory.

cd into project directory
```
cd ../my_project_dir
```
install ahlev-django-auth-rename from the project directory
```
pip install ../ahlev-django-auth-rename/dist/ahlev-django-auth-rename-0.0.1.tar.gz
```

## install from pypi
[ahlev-django-auth-rename](https://pypi.org/project/ahlev-django-auth-rename/)

## project configuration
### update settings.py as the following
```
INSTALLED_APPS = [
    'auth_rename', # add this line, and comment the below
    #'django.contrib.auth', 
]
```

## screenshots
### backend: user management
![](screenshot/auth_rename_backend1.png)