### 1. Decorator
>- 함수를 받아서 함수를 return하는 함수
>    * python에서는 함수도 객체다!
>- 기본 Frmae은 다음과 같다
> ```python
 __dic={}
 def memo_fib(n):
     print(__dic)
     if n in __dic:
         return __dic[n]
     else :
         __dic[n]=n if n < 2 else memo_fib(n-2)+memo_fib(n-1)
         return __dic[n]
 memo_fib(3)
> ```
- 위의 함수를 다음과 같이 변경할 수 있다.

```python
def memoize(func):
    __cache={}
    def wrapper(args):
        print(__cache)
        
        if args in __cache:
            return __cache[args]
        else:
            return __cache.update({args:func(args)}) or __cache[args]
            #__cache[args]=args if args < 2 else func(args-2)+func(args-1)
            #return __cache[args]
    return wrapper
    
@memoize
def deco_fibo(n):
    return n if n < 2 else deco_fibo(n-2) + fibo(n-1)
```

#### decorator는 밑에서부터 적용 된다.
>```python
@test1
@test2
@test3
def func_test():
>```
>- 위의 경우 test3 > test2 > test1의 순서로 적용된다.