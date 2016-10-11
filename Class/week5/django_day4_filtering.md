## django 4th day

### organize class hour 

1. select 시 filtering
 
>- filter : 조건 해당하는 여러 값만 / get : 조건에 해당하는 하나의 값만
>- exclude : 조건에 해당하지 않는 값만 
>- Field name에 _를 두개 붙여주면 Field의 속성에 접근 가능
>- chaining filtering이 가능함 (filtering결과를 변수에 담아서 다시 filtering하는 도 가능함)
>
>>```python
>>Entry.objects.filter(pub_date__year=timezone.now().year).exclude(headline__contains="test")
>>```
>
>- 쿼리셋을 선언할 경우 선언만 하고 있다가, print를 하는 순간 DB에서 조회하게 됨
>- all()했을 경우 query set에 답기는 순서는, id혹은 meta class에서 설정한 ordering값의 대소에 따라 정해짐
>- list slicing기법이 모두 가능하니 잘 사용해 볼 것
>  
  
2. Field Filtering
 
>- 1. Field lookup
>
>>- lookup key 앞에 __가 필요함
>>- exact / iexact : 일치하는 것 / 대소문자 관계 없이 일치하는 것
>>- contains / icontains : 포함하고 있는 것 / 대소문자 관계 없이 포함하고 있는 것
>>```python
>> Entry.objects.get(headline__exact="Cat bites dog")
>> Entry.objects.get(headline__icontains="BiTes")
>>```
>>
>>- lte(<=) / gte(>=) / lt(<) / gt(>) / eq(==)
>>```python
>> Entry.objects.filter(pub_date__lte='2006-01-01')
>>```
>>
>
>- 2. F expression F(Field)
>
>>- 바로 값을 가져옴(Table의 Field를 따로 호출하지 않고)
>>- F([Field_Name])으로 사용
>>- 비교문 뿐 만 아니라 update에도 편리함
>>- query set을 변수에 담고 list comprehension 사용이 가능함
>>```python
>> from django.db.models import F
>> # Entry Table에서 blog를 호출하여 name에 접근하지 않았지만, 조건식이 작동
>> Entry.objects.filter(authors__name=F('blog__name'))
>> # or
>> Entry.objects.filter(pub_date__lt=F('create_date'))
>>```
>
>- 3. Q Expression Q(Condition)
>
>>- and / or연산의 경우 Q expression을 통해 조건을 형성
>>- Q(필터문), (and) Q() | (or) Q() 이런식으로 
>>- kwargs가 있는 경우 맨 뒤로 뺀다 (*중요)
>>```python
>>from django.db.models import Q
>>Poll.objects.get(
>>    Q(question__startswith='Who'),
>>    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
>>)
>>
>># kwargs와 사용할 경우 kwargs를 뒤로 빼준다
>>Poll.objects.get(
>>    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
>>    question__startswith='Who',
>>)
>>```
>
>- 4. 필터 조건에 따라 값이 다른 경우가 발생
>
>>```python
>> # type 1
>> Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
>> # type 2
>> Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
>>```
>
>>- 1. #type 1의 경우 and를 이용해 두 조건을 동시에 만족하는 경우 filtering
>>- 2. #type 2의 경우 먼저 entry에 Lennon을 포함하는 Blog를 먼저 검색한 후, 그 Blog들 사이에서 pub_date가 2008년인 entry를 포함하고 있는지 다시 filtering함. 즉, 첫 번쨰 조건을 만족시켰기 때문에 두 번쨰 조건은 첫 번째 조건에 영향을 받지 않음.
>

3. Caching Queryset

>- Queryset을 만들었을 때는 cache가 비어있음.
>- Queryset이 DB에 access하고 난 후 결과가 cache에 저장.
>- 1. 이후 동작하는 Queryset은 cache를 재사용하게 된다.
>
>>```python
>> queryset = Entry.objects.all()
>> print([p.headline for p in queryset]) # Evaluate the query set.
>> print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.
>>
>> queryset = Entry.objects.all()
>> [entry for entry in queryset] # Queries the database
>> print queryset[5] # Uses cache
>> print queryset[5] # Uses cache
>> 
>> bool(queryset) # Uses cache
>> entry in queryset # Uses cache
>> list(queryset) # Uses cache
>>```
>
>- 2. 일부만의 결과를 받는 경우 cache를 사용하지 않음(list slice / use index)
>- query set을 slicing할 경우 다시 DB I/O가 발생하게 됨
> 
>>- 
>>```python
>> queryset = Entry.objects.all()
>> # Print시 DB에 Access 됨
>> #Slicing의 경우 전체 queryset list에서 slicing되는 것이 아니라, slicing한 객체만 return하도록 query문이 생성되어 DB에 Access함.
>> print(queryset[5]) # Queries the database
>> print(queryset[5]) # Queries the database again
>>```
>


>- FK는 단순히 변수에 값을 넣는다고 하여 같이 복사되지 않는다.(mtm Field 등)
>- 이유? 
>- 해당 table의 데이터만 복사
>- 즉 mtm table까지는 복사가 되지 않음
>- 때문에, mtm필드의 내용을 all()로 전부 담아주어야 한다.

>- clear()는 연결관계만을 삭제, delete()는 연결된 요소까지 삭제

* {% load static %} or {% load staticfiles %}
>- static root를 참조하기 or staticfiles_dirs에 선언한 모든 static directory 참조하기
