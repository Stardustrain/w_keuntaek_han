##django.db.models.Model

### 1. django의 model은 DB의 data와 연관이 있다.
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
 
### 2. models 사용

- settings.py file의 INSTALLED_APPS부분에 ```'[app name]'```을 선언해야 함
- models.py  file내의 변경으로 DB의 변경이 발생하면 반드시 ```makemigrations``` > ```migrate``` 순으로 변경 사항 반영

---

### 3. Field

-  Field는 class 내의 attribute 형태로 선언되며, DB에 columns로 insert 됨
- [Field Type](https://github.com/Stardustrain/w_keuntaek_han/blob/master/Class/week4/django_model_field.md)
- Field options

> 1. null
>> - 비어있는 값인 NULL을 DB에 저장
>
> 2. blank
>> - NULL값이 DB에 저장되는 것이 아니라, 해당 column 자체가 값이 비어 있게 됨
>> - True일 경우 값이 비어있는 것이 허용되며, False일 경우 값을 반드시 채워 넣어야 함
>
> 3. choices
>> - elements를 가진 iterable한 tuple을 field의 choices 옵션에 선언 해 줄 수 있음
>> - tuple의 첫 요소가 DB에 저장되고, 두 번째 요소는 get_[tuple_name]_display()로 호줄이 가능 함
>> ```python
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
>> ```
>> ```
p = Person(name="Fred Flintstone", shirt_size="L")
p.save()
p.shirt_size
-> 'L'
p.get_shirt_size_display()
-> 'Large'
>> ```
>
> 4. default
>> - Field의 default값을 설정 함
> 
> 5. primary_key
>>  - 해당 Field를 pk로 사용함
>> - `primary_key=True` 옵션이 없으면 자동으로 IntegerField를 생성 함(Automatic primary key Field)
>> - ```python
id = models.AutoField(primary_key=True)`
>> ```
>
> 6. unique
>> - 해당 Field에 unique(중복값 허용 안함) 속성을 부여함

- Verbose Field names

> - "읽기좋은" 형태의 필드 이름
> - Verbose name이 없으면 자동으로 `_`문자를 제외하고 verbose name을 만들게 됨
> - ForeignKey, ManyToManyField, OneToOneField를 제외하고 Field 선언 시 첫 번째 argument에 verbose name을 부여할 수 있음
> ```python
first_name = models.CharField("person's first name", max_length=30)
>```
> - ForeignKey, ManyToManyField and OneToOneField의 경우 verbose_name 옵션을 따로 선언해야 함
> ```python
poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    verbose_name="related place",
)
>```

---

### 4. Relationships

- Many-to-one (1 : 다 관계)

>- 특정 Table의 PK를 다수의 Table이 참조(FK)하는 경우.
>- ForeignKeyField를 사용
>- e.g.) 특정 공장과 그 공장에서 생산된 자동차의 관계
>>- 특정 공장의 일련번호(PK)가 그곳에서 생산된 자동차의 프레임에 찍히는(FK)경우
>
> ```python
from django.db import models
class Manufacturer(models.Model):
    # ...
    pass
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...
>```
>

- Many-to-Many (다 : 다 관계)

>- 각 테이블의 PK가 다른 테이블의 FK로 참조. 
>- 하나 이상의 PK가 FK로 관계를 맺음
>- 영화 테이블과 영화배우 테이블 간의 관계
>- ManyToManyField를 사용 
>- ManyToManyField 사용 시 django가 알아서 Table을 생성함
>- m1, m2테이블이 있다고 가정하면, 

>>- m1과 m2 테이블의 PK를 새로운 m3이라는 테이블에 저장
>>- m1과 m2는 m3의 PK를 FK로 참조하게 됨
>
>
