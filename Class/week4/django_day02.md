## django 2nd day

### organize class hour

1. request의 return 이유?
>- 사용자의 session 정보 등을 주고 받음
>- django에서는 middleware에서 자동으로 session을 구현해 줌

2. application의 app.py?
>- app의 자세한 정보를 전달하고자 할 때 사용

3. SQL - ORM
>- ```python manage.py sqlmigrate [app_name] [migrate number (e.g. 0001)]```
>- QuerySet은 list type으로 return
>
>>- objects.get([조건]) : 하나의 결과만을 가져옴
>>- objects.filter([조건]) : 여러 결과를 가져옴
> 
> primary_key로 선언된 field는 id혹은 pk로 접근 가능함
>- fk가 포함된 model의 값 추가
>
>>- fk 필드 부분에 관련 model obj를 그대로 넣어준다
>>- e.g : Question PK --> Choice question: FK
>>```python
q = Question.objects.get(pk=question_id)
>>c = Choice.objects.create(question=q, choice_text='test', votes=0)
>>c.save()
>>``` 
>

4. reverse의 의미
>- hardcoding이 된 url이 아닌 namespace 및 name을 보고 역으로 찾아오는 것
> e.g.
>```python
> 1. {% url 'polls:vote' %}
> 2. reverse(request, 'polls:vote', ret)
>```