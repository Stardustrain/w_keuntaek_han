## django 4th day

### organize class hour

**OOP스럽게 생각해보자**
**실습 필수! 코드와 함꼐 정리할 것**

1. one-to-one Relationship 

>- [day03](https://github.com/Stardustrain/w_keuntaek_han/blob/master/Class/week4/django_day03.md) 참고
>- 다른 모델을 확장하여 사용할 때, 
>
>>- e.g)유저의 이름과 상세 프로필을 테이블을 나누어 관리할 때
>
>- related_name option
>
>>- **역참조**시 피참조 테이블의 Field 값을 호출시 사용하는 일종의 변수명
>>- 특정 테이블의 Field들이 다른 하나의 테이블을 참조하고 있는 경우, 모두 같은 테이블을 참조하고 있어 어느 Field를 역참조 해야하는지 명확히 알려줌
>
>>```python
>> class Auth(models.Model):
>>     auth_mode = models.CharField(max_length=20)
>>
>>
>> class User(models.Model):
>>     auth = models.OneToOneField(Auth, on_delete=models.CASCADE)
>>     user_id = models.CharField(max_length=30)
>

2. Model의 참고 사항들

>- 다른 app의 model을 참조
>>- 필요한 app의 Model class를 import하여 사용함
>
>- Field name에 절대 _를 두 개 쓰지 않음

3. Custom Field Types
 
>- [실습](https://docs.djangoproject.com/en/1.10/howto/custom-model-fields/)해볼것
 
 4. Meta options
 
>- Model 자체에 대한 설명
>- Model Class 안에 `class Meta :` 로 선언해 주고, 옵션을 주게 됨(정렬 순서의 기본값 등)
>
>> -자주 쓰일 것 같은 options
>> 1. ordering - 정렬
>>```python
>> class A(moels.Model):
>> ...
>>    class Meta:
>>        ordering = ['pub_date'] # ['-pub_date']로 역순도 가능함
>>```
>>
>> 2. abstract - 추상 클래스 선언
>>```python
>> class B(models.Model):
>> ...
>>     class Meta:
>>        abstract = True
>>```
>
 
 5. model manager
 
>- objects가 기본으로 선언됨
>- manager 함수를 따로 만들어 model class 안쪽에 선언하여 사용이 가능함
>- 자주 사용하는 query를 만들어 사용하면 편함
>
>>```python
>> class DahlBookManager(models.Model):
>>     def get_queryset(self):
>>         return super(DahlBookManager, self).get_queryset().filter(name="Dahl")
>>
>>
>> class Book(models.Model):
>>     title = models.CharField(max_length=100)
>>     author = models.CharField(max_length=50)
>>
>>     objects = models.Manager()
>>     d_objects = DahlBookManager()
>>```
>
 
 6. model method
 
>- model의 instance 단위로 함수를 만들어줌
>>- field에 f_name, ㅣ_name이 있는 경우 get_fullname 함수를 만들어 이름을 연결하여 return하는 등...
>
>>```python
>> class User(models.Model):
>>    auth = models.OneToOneField(Auth, on_delete=models.CASCADE)
>>    user_id = models.CharField(max_length=30)
>>    first_name = models.CharField(max_length=30)
>>    last_name = models.CharField(max_length=30)
>>
>>    @property
>>    def full_name(self):
>>        return "{f_name} {l_name}".format(f_name=self.first_name,
>>                                           l_name=self.last_name)
>>```
>
>>```python
>> u1 = User.objects.first()
>> u1.full_name
>>```
>
 
 7. predefine Methods cunstomizing
 
>>- save()를 overriding을 하는 등...
>>- username이 admin인 경우 저장 안함 설정
>>- 상위 클래스의 메소드를 반드시 상속받아야 함.
>>- super([model class name], self).save(*arg, **kwargs)
>
>>```python
>> class Blog(models.Model):
>>    name = models.CharField(max_length=100)
>>    tagline = models.TextField()
>>
>>    def save(self, *args, **kwargs):
>>        do_something()
>>        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
>>        do_something_else()
>>```
>

 8. raw SQL도 cuntomizing하여 사용함
 
>- objects.raw([Query]);로 사용 가능함
 
 9. Model class의 상속
 
>- 1. 테이블 생성
>
>>- 부모 model에 대한 상속
>>- 부모 table은 그대로 생성됨
>>- 자식 테이블은 부모 테이블를 참조하는 id값과 자신의 field값을 가지게 됨
>>- 일반 상속관계 처럼 사용이 가능
>>- 자식 클래스에서 data 생성
>
>- 2. 개념
>
>>- 부모 class가 abstract인 경우 자식 class에서 상속받아 구체적인 구현을 하게 됨
>>- abstract인 경우 부모클래스에서 query실행이 불가능 함
>>- 자식의  meta class가 없으면 부모의 meta class를 상속받음
>>- overriding이 가능함
>>- 부모에서 자식 참조시 [부모인스턴스].자식테이블(lowercase).[fieldname] 이렇게 참조
>
>>```python
>> class Common(models.Model):
>>    name = models.CharField(max_length=100)
>>    age = models.IntegerField()
>>
>>    class Meta:
>>        abstract = True
>>
>>
>>class Student(Common):
>>    group = models.CharField(max_length=5)
>>```
>
 
10. Proxy Model
 
>- table은 그대로 두고 함수, 출력 qeury 등을 다르게 하고 싶을 때
>- Field값은 부모의 Field만을 참조하게 됨
>- 자신의 Field를 갖지 않는 Proxy 개념의 테이블이라고 생각하면 될 
 
11. 다중상속
 
>- 다중 상속 시 id값을 구분하기 위하여 부모 클래스들의 id값을 구분 가능한 이름으로 수동 선언 해줌
>- 그래서 id값이 없는 추상클래스를 이용해 다중상속 하는 것이 유리함
 
12. FK바꾸기
 
>- 필드명으로 접근하여 인스턴스 변수를 넣어줌
>>- FK 필드명이 name이면, name=[인스턴스변수]
>
>- save()전 까지 DB에 반영되지는 않음
>
 
13. mtm Field 값 추가
 
>- add를 이용해 여러 값을 한번에 넘겨 주어도 상관없음