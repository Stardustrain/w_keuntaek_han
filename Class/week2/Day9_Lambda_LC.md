### 1. List Comprehension
>- List안에 Function이 포함<br>
> [ 연산 for ___________ ]
> ``` python
> [i * 2 for i in range(5)]
>```

***

### 2. Lambda Operator
>- 함수형 프로그래밍 구현이 가능함
>- Lambda는 return을 명시하지 않아도 좋음

#### map
>- Elements에 대해 동일한 함수를 적용함
>- map(함수, iterable한 객체)
>- list(map()) << 이런 형태로 자주 사용함
>- 적용 함수 부분에 lambda를 잘 쓰면 함수를 정의할 필요도 없다

#### filter
>- Elements를 필터링
>- filter 조건에 맞는 값들만 list로 return하는 등의 방법
>- filter(조건(보통 lambda식, iterable한 객체)

#### reduce
>- import하여 사용
>- list가 아닌 value값 하나가 결과로 나오게 됨
>- list가 아닌 max, min처럼 하나의 결과가 나오는 로직에서 유리함
>- reduce(whrjs, iterable한 객체)
>- reduce는 조건에 if, else 등을 사용할 수 있음

***

### 3. *args, **kwargs
#### *args
>- parameter의 개수를 가변적으로 받고 싶을 때
>- 복수 개수의 parameter를 tuple로 받아서 한꺼번에 넘겨줌 (pack)
>- 함수 호출 시 인자 부분에 *와 함께 호출 > parameter가 하나씩 넘어감 (unpack)

#### **kwargs
>- parameter의 이름을 지정하여 dic의 형태로 받을 수 있음

#### *args와 **kwargs를 동시에 사용했을 시
>```python
> def test(*args, **kwargs)
>     print(args)
>     print(kwargs)
>
> test(1,2,3, name="test")
>```
>- 각 인자의 출력 결과는
>```python
> (1,2,3)
> {"name" : "test"}
>```