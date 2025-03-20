## 0. setting

- `.gitignore`
- 가상환경 설정
    - `python -m venv venv`
    - `source venv/Scripts/activate`
- `README.md`

## 1. Django

1. django 설치
```shell
pip install django
```

2. 프로젝트 생성
```shell
django-admin startproject <pjt-name> <path>
```

3. 서버실행 (종료 : `ctrl + c`)
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app-name>
```

5. 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```

## 2. CRUD
- modeling (`models.py`)

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

- migration (`migrations`)

```shell
# 번역본 생성
python manage.py makemigrations

#DB에 반영
python manage.py migrate 
```

- create super user
```shell
python manage.py createsuperuser
```

- admin에 모델델 등록 (`admin.py`)
```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```