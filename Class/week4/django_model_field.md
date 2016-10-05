##django.db.models.Model

### Filed type

>1. **AutoField**

>	1\. IntegerField는 ID(PK)가 자동으로 증가함

>	2\. BigIntergerField는 64bit의 integer변수의 init을 지원함

>2. **booleanField**

>	1\. T / F를 구분하는 field.

>	2\. 만약 Null을 허용하고 싶다면 NullBooleanField 사용

>3. **CharField(max_length)**

>	1\. 작은 사이즈의 String을 init

>	2\. 많은 양의 text는 TextField를 사용함

>4. **CommaSeparatedIntegerField(max_length)**

>	1\. CSV형식으로 숫자를 구분

>5. **DateField(auto_now, auto_now_add)**

>	1\. python의 ```datetime.date``` 인스턴스를 표현

>	2\. auto_now
>>		obj가 변경될 때 마다 자동으로 변경됨
>>		Model.save() , QuerySet.update() 시 modify 됨
> 
>     3\. auto_now_add	
>> obj가 처음 생성 되었을 때만 create 됨
>
> 6. **DateTimeField(auto_now, auto_now_add)**

>	1\. python의 ```datetime.datetime```인스턴스를 표현

>7. **DecimalField(max_digits, decimal_places)**

>	1\. 정확한 실수 표현을 위한 field

>	2\. 정수의 자리수(max_digits)와 실수의 자리수(decimal_places)를 설정할 수 있음

>8. **DurationField**

> 	1\. python의 ```timedelta```로 시간의 경과를 저장

>9. **EmailField**

>	1\. CharField형식이지만, email의 valid를 체크함

>10. **FileField(upload_to, max_length)**

>	1\. PK와 unique parameter는 지원하지 않으며, 사용할 경우 TypeError 발생

>	2\. upload_to
>>    - upload 디렉토리와 file name을 set 할 수 있는 방법을 제공함
>>    - default 저장 경로는 ```MEDIA_ROOT``` 경로임
>>    - 저장 경로 변경 시 사용함 
>> ```python
class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')```
>> 
