## django 3rd day

### organize class hour

1. django Debugging
>- from IPython import embed(); embed();

2. Models
>- 1. 중복 data는 따로 테이블을 만들어서 관리
>- 2. ForeignKey는 Null값을 허용하지 않음! -> DB에 아무 값도 없는 상태에서 migrations시 FK Field를 migrate하려고 하면 문제가 발생함!
>
>>- 해당 경우는 CREATE가 아닌 ALTER로 SQL문이 전송됨
>>- null = True / default = '[default value]' / blank = True : 해당 방법들로 해결이 가능함 
>>- DB는 가능하면 한번에 migration 할 것
>
>- 3. pk는 겹치지 않으며, Null을 허용하지 않는다.
>
>>- AutoField로 선언해 준다.
>>- pk를 명시해 주지 않을 경우 id 필드를 AutoField로 자동생성
>
>- 4. django에서는 기본적으로 각 Field에 Null을 허용하지 않는다.
>
>>- model의 API와 같은 이름을 field에 만들지 않는다.

3. Field options
>- 1. 공통옵션
>
>>- null : DB에서의 null값
>>- blank : django에서의 빈 문자열을 의미함
>>- choices : DB에는 짧은 문자열이 들어가고, django상에서는 mapping한 문자열로 표현이 가능함
>- default
>- help_text : 문서 만들기 및 teml widget을 만들 때 사용 함
>- PK : PK는 기본적으로 ReadOnly기 때문에 이미 save()한 객체를 바꾸려고 하면 새로운 값으로 insert 됨
>

4. Relationship
>- 1. m : 1 관계
>
>>- ForeignKey Field를 통해 만들어짐
>>- CASCADE : PK가 삭제되면 FK로 연결된 값들도 같이 삭제됨
>
>- 2. m : m 관계
>
>>- 서로 1개 이상의 PK를 FK로 참조하고 있는 경우
>>- ManyToManyField를 통해 만들어짐
>>- 해당 필드를 선언하는 테이블은 관념적으로 자연스러운 쪽에 선언
>>
>>>- e.g : pizza, toppnig 두 테이블이 있을 경우 pizza에 topping을 manytomany 필드로 정해준다.(피자에 다수의 토핑이 올라감)
>>>- mtm Field를 선언하면, ```[app name]_[tanble1]_[table2]``` 모양의 table이 생성되며, 이 table은 각 table의 matching값을 저장하게 됨
>>- 예시
>>
>>> 1. pizza의 값을 생성하여 save할 시 mtm 필드의 값을 채워 줄 필요가 없음
>>> 2. pizza의 인스턴스를 선언한 뒤, .add([toppings instance])방식으로 값을 더해줌
>>> 3. pizza의 인스턴스에서 topping.values_list()명령어로 값을 불러옴.
>>> 4. 반대로, mtm필드가 없는 쪽에서도 역참조가 가능함. 
>>> 5. 값이 cascade로 얽혀있는 관계가 아니라서, 하나가 삭제되어도 관계된 값이 사라지지 않는다.
>>>
>>> 정리하자면, 

>>>```python
class Toppings(models.Model):
    title = models.CharField(max_length=20)
class Pizza(models.Model):
    title = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Toppings)
>>>```

>>>```python
>> p1=Pizza.objects.create(title='치즈피자')
>> p1.save()
>> t1 = Topping.objects.create(title='치즈')
>> t1.save()
>> t2 = Topping.objects.create(title='페퍼로니')
>> t2.save()
>> p1.toppings.add(t1, t2)
>> #출력
>> p1.toppings.values_list('title')
>> #역참조
>> t1.pizza_set.values_list('title')
>>>```
>
>- 3. Extra field on m : m relationships
>
>>- 두 테이블간의 관계에서 끼어들기 어려운 값을 다른 테이블로 생성해 줌
>>- mtm field에 through=[다른 테이블 이름] 옵션으로 주어 참조하게 만든다
>>- Extra Field의 경우 값 변경시 반드시 중간자 테이블에서 값을 넣어주어야 함
>> 모든 테이블간의 역참조가 가능함)