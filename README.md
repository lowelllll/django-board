# django-board
2018년 수행평가 - 게시판 만들기



## 서버 띄우기

python3, pip(version 3)가 설치되어있어야 함.



- 가상환경 셋팅

```
$ python -m venv ./devenv # 가상환경 생성
```

현재 디렉토리에 devenv파일 확인,



-  가상환경 활성화

```
$ devenv\Scripts\activate 
(devenv) $ # 이렇게 prompt 앞에 가상환경이 표시되는 것을 확인.
```



- 패키지 설치

```
(devenv) $ cd django-board # 프로젝트 폴더로 이동
(devenv) django-board $ dir
... requirements.txt # 해당 디렉토리에 requirements.txt가 있는지 확인
(devenv) django-board $ pip install -r requirements.txt # 의존되어있는 패키지 설치
```



#### Django 셋팅

- 데이터베이스 연동

```
(devenv) django-board $ dir
... manage.py # manage.py가 있는 폴더가 프로젝트 디렉토리
(devenv) django-board $ cd board 
(devenv) django-board/board $ vi settings.py # settings.py를 vi편집기로 수정
```

board/settings.py

```python
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your-databasename',
        'USER': 'root', # your-database user
        'PASSWORD': 'your-password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

```

settings.py에서 DATABASES 블록에서 자신의 MySQL 셋팅에 맞게 수정 (NAME,USER,PASSWORD) 

host와 port도 필요에따라 수정 가능.

- DB 반영

```
# 다시 manage.py 가 있는 곳으로 이동
(devenv) django-board/board $ cd .. 
(devenv) django-board $ python manage.py migrate
```

오류가 안나면 성공!

- 어드민 유저 생성

```
(devenv) django-board/board $ python manage.py createsuperuser
username: ...
...
... 
```

- 드디어 실행

```
(devenv) django-board $ python manage.py runserver 
```

localhost:8000번 포트로 이동하면 서버가 켜져있는 것을 확인하실 수 있을겁니당 