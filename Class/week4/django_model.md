##django.db.models.Model

##### 1. django의 model은 DB의 data와 연관이 있다.
> 아래 코드를 SQL에 대입하면 다음과 같다.
>
> python
> ```python
> class Person(model.Model):
>     name = models.CharField(max_length=30)
> ```
>
> SQL
> ``` 
> CREATE TABLE myapp_person('id' serial NOT NULL PRIMARY KEY, 'name' varchar(30) NOT NULL)
>```

- Table name은 ```[app name]_[class name]```으로 정해짐
- id는 자동으로 pk선언 됨
 
---
 
##### 2. models 사용

- settings.py file의 INSTALLED_APPS부분에 ```'[app name]'```을 선언해야 함
- models.py  file내의 변경으로 DB의 변경이 발생하면 반드시 ```makemigrations``` > ```migrate``` 순으로 변경 사항 반영
