
# coding: utf-8

# ## 1. Decorator

# In[1]:

# 함수의 실행 시간을 측정하는 함수를 만들어 보자

def hello(name):
    print("hello {name}".format(name=name));


# In[4]:

# 1. 기초단계
# 해당 함수의 앞 뒤로 시간 측정 구문을 넣어보는 것

import time
start_time=time.time()
hello("han")
end_time=time.time()

print("Execute time : {time}".format(time=end_time-start_time))


# In[5]:

# 문제점?
# 1. 하나의 함수를 측정하기 위해 많은 양의 코드가 사용됨
# 2. 재사용성이 떨어짐

# 2. 새로운 함수를 생성하여 그 안에서 기존 함수를 call

def new_hello(name):
    start_time=time.time()
    hello(name)
    end_time=time.time()

    print("Execute time : {time}".format(time=end_time-start_time))


# In[7]:

new_hello("han")


# In[9]:

# 문제점?
# 1. 기존 함수를 제외하고 새로운 함수를 call 해야 함
# 2. 시간 측정 부분의 재사용성이 떨어짐
# 3. 함수 수정 시 두 함수를 모두 수정해야 함

# 3. 파이썬은 모든 것이 객체다! 함수도 return 시켜 보자!
# 일단은 테스트 코드

def get_multi(n):
    def return_func(x):
        return x * n
    return return_func

testA=get_multi(2);   # return_func(x) return x * 2 의 상태로 리턴
print(testA)
testA(100)    # return_func(100) return 100 * 2 값이 반환


# In[11]:

# 본격적인 decorator 코드를 만들어 보자

def time_track(func):
    def wrapper(*args, **kwargs):   # wrapper는 리턴 함수의 관념적인 이름
        start_time=time.time()
        func(*args, **kwargs)
        end_time=time.time()
        print("Execute time : {time}".format(time=end_time-start_time))
    return wrapper

hello_=time_track(hello) # wrapper의 func에 hello가 들어간 상태로 리턴
hello_("Lee") # wrapper가 그대로 실행됨


# In[14]:

@time_track # decorator는 함수를 return받고 return받은 변수를 실행해 주는 과정을 자동화
def deco_hello(name):
    print("hello {name}".format(name=name));
    
deco_hello("HI")


# In[27]:

# 다수의 Decorator를 적용해 보자
def start_func(func):
    def wrapper(*args, **kwargs):
        print("start func")
        return func(*args, **kwargs) # 실행순서가 start > end > multi 라면 
    return wrapper                   # return은 겹치는 건가? 출력위치도 겹칠테니...

def end_func(func):
    def wrapper(*args, **kwargs):
        res=func(*args, **kwargs) # 함수를 먼저 실행해 결과를 미리 담고
        print("end func") # end를 출력
        return res; # 함수 실행이 끝난 후, 실행 결과를 return한다
    return wrapper


@end_func    # decorator의 적용순서는 밑에서 위의 순서
@start_func
def multi_deco_hello(name):
    return "hello {name}".format(name=name);
    


# ## 2. histogram 출력해보기

# In[66]:

data=["fast", "campus", "fast", "campus", "school", "fast", "fast"]

def hist_data(arr):
    res={}
    
    for i in set(arr):
        res[i]=0
        
    for i in arr:
        res[i]+=1
    
    for i in res:
        print("{key}\t{val}".format(key=i, val="="*res[i]))

hist_data(data)


# In[67]:

# LC로 출력해보기

def hist_data_lc(arr):
    res={}
    
    for i in set(arr):
        res[i]=0
        
    for i in arr:
        res[i]+=1
    
    # 위의 출력값은 결국 
    # campus\t==\nfast\t====\nschool\t=\n 과 같다
    # 즉, \n을 기준으로 묶여있는 상태
    
    print(
    "\n".join([
                "{key}\t{val}".format(key=i, val="="*res[i])
                for i in res
            ])
    )
    
hist_data_lc(data)


# In[69]:

# Lambda로 출력해보기

def hist_data_lambda(arr):
    res={}
    
    for i in set(arr):
        res[i]=0
        
    for i in arr:
        res[i]+=1
    
    print(
        "\n".join(
            map(
                lambda x: "{key}\t{val}".format(key=x, val="="*res[x]), res
            )
        )
    )
    
hist_data_lambda(data)


# 
# ## 3. sort + lambda

# In[49]:

data=[5,2,4,1,6,3]

sorted(data)


# In[62]:

# tuple의 경우 key값 (x[0])을 기준으로 오름차순 정렬 > list return

before_tu=[("python",30), ("ruby",20), ("javascript",50)]

# vlaue를 기준으로 정렬 할 수도 있다.
# key값은 callable한 객체가 필요함
print(sorted(before_tu, key=lambda x : x[1]))


# In[74]:

dic_data={'campus': 2, 'fast': 4, 'school': 1}

sorted(dic_data, key=lambda x: dic_data[x])


# In[77]:

print(
    "\n".join([
                "{key}\t{val}".format(key=i, val="="*dic_data[i])
                for i
                in sorted(dic_data, key=lambda x: dic_data[x])
            ])
    )


# ## 4. 재귀함수

# In[80]:

# 1. 팩토리얼

def factorial(n):
    if n == 1:
        return 1;
    return n * factorial(n-1)

factorial(3)


# In[94]:

# 2. 피보나치 수열

def fibo(n):
    prev, cur = 0, 1
    
    if n==0:
        return 0
    
    for i in range(n-1): # n이 2일 때 부터 시작
        '''
        tmp = prev + cur
        prev = cur
        cur = tmp
        '''
        prev, cur = cur, prev + cur
    return cur

fibo(3)


# In[97]:

# 결국 피보나치 수열은 알고싶은 자리 n의 2자리 앞과 1자리 앞을 더한 것임
# fibo(n)이 n자리의 값을 알고 싶은 것 이라면,
# fibo(n-2) + fibo(n-1)

def fibo_dev(n):
    '''
    피보나치 수열의 0과 1 자리의 값은 index와 동일하게 0, 1
    if n==0 or n==1:
        return n
    '''
    
    '''
    이 조건문도 return에 합쳐 본다
    if n<2:
        return n
    '''
    return n if n<2 else fibo_dev(n-2) + fibo_dev(n-1)

fibo_dev(3)


# In[99]:

# 위의 재귀함수는 메모리 낭비가 심하기 때문에 
# 결과값을 저장해두는 방법을 사용한다 (memoization) << 오타가 아님!


# ## 5. 동적계획법 (Dynamic Programing: 기억하며 풀기)

# In[100]:

# 큰 문제를 작은 문제로 구분하여 해결
# cache라는 공간에 연산결과를 저장해 놓고
# 이전에 연산한 결과가 있으면 cache에서 return 해준다


# In[120]:

# 호출순서 물어 볼 것!

__dic={}
def memo_fib(n):
    print(__dic)
    if n in __dic:
        return __dic[n]
    else :
        __dic[n]=n if n < 2 else memo_fib(n-2)+memo_fib(n-1)
        return __dic[n]


# In[122]:

memo_fib(3)


# In[142]:

def memoize(func):
    __cache={}
    def wrapper(args):
        print(__cache)
        
        if args in __cache:
            return __cache[args]
        else:
            __cache[args]=args if args < 2 else func(args-2)+func(args-1)
            return __cache[args]
    return wrapper


# In[143]:

@memoize
def deco_fibo(n):
    return n if n < 2 else deco_fibo(n-2) + fibo(n-1)


# In[153]:

deco_fibo(3)


# In[163]:

# dic의 함수 중 update({k:v})가 있음
# 해당 함수의 return값은 None임
# None은 False를 return 함

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


# In[164]:

@memoize
def deco_fibo(n):
    return n if n < 2 else deco_fibo(n-2) + fibo(n-1)


# In[168]:

deco_fibo(6)

