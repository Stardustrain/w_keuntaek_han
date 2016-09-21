
# coding: utf-8

# In[2]:

########## Lambda = LD / List Comprehension = LC
# 1. 조건문 범위 지정
res=[];

for i in range(10):
    # ()가 없을경우, 인터프리터는 실행범위를 내부적으로 fix하게 됨
    # "fast" if (i+1)%3==0 else "" + "campus"
    # 그렇기 때문에 3의 배수가 아니면 ""+"campus"가 출력되는 것임
    # 때문에, 조건을 ()를 통해 block 지정을 해 주는 것이 중요함
    # 따로 조건을 계산해 주기 위해서 ()를 해주게 됨
    element=("fast" if (i+1)%3==0 else "") +         ("camp" if (i+1)%5==0 else "")
    res.append(element)
    
res


# In[13]:

# 2. 소수 구하기
def isPrime(number):
    for i in range(2, number):
        if number%i==0:
            return False
    return True

# assert는 미리 함수를 테스트해 볼 수 있는 함수
assert isPrime(2) == True


# In[17]:

def get_prime(n):
    arr=[]
    for i in range(2, n):
        if isPrime(i):
            arr.append(i)
    return arr

get_prime(10)


# In[21]:

# 3. tuple로 parameter 받기
# 1의 함수를 수정
# tuple을 []로 묶어서 받을 수 있음

def tuple_parameter(n, rule1, rule2):
    arr=[];
    for i in range(n):
        text=""
        for rule in [rule1, rule2] :
            #div, val = rule
            text+=rule[1] if (i+1)%rule[0]==0 else ""
        arr.append(text)
    return arr

tuple_parameter(10, (3, "fast"), (5, "campus"))


# In[26]:

# 4. List의 모든 합과 max값 구하기

def get_sum(arr):
    res=0;
    for i in arr:
        res+=i
    return res

get_sum([1,2,3,4])

def get_max(arr):
    res=arr[0]
    for i in arr:
        if i > res:
            res = i
    return res

get_max([-1,-2,-3,-4,-1])


# # 1. Lambda Operator / List Comprehension

# ## 1. map

# In[30]:

# 5. Lambda Operator
# 5-1. map

# List를 입력받아 모두 2를 곱해주는 map

list(map(lambda x: x * 2, [1,2,3,4]))

# 3의 결과를 횟수를 입력받아 Lambda Operator로 표현
list(map(lambda x: ("fast" if (x+1)%3==0 else "") +                     ("camp" if (x+1)%5==0 else "")
         , range(10)))


# In[32]:

# List Comprehension
[
    ("fast" if (x+1)%3==0 else "") + \
    ("camp" if (x+1)%5==0 else "")
    for x
    in range(10)
]


# ## 2. filter

# In[41]:

# List를 입력받아 양수만 반환

data=[1,-2,3,-5]
# 함수
def get_pos(arr):
    res=[];
    for i in arr:
        if i > 0:
            res.append(i)
    return res

get_pos(data)

# Lambda
list(filter(lambda x: x > 0, data))

# List Comprehension
[
    i
    for i in data
    if i>0
]


# In[20]:

# sum_fifth
# 1~10의 배열을 입력받아 제곱한 후, 그 값이 50이 넘는 값만 출력
def sum_fifth():
    arr=[]
    for i in range(1, 11):
        if i**2 > 50:
            arr.append(i**2);
    return arr

sum_fifth()

# Lambda
def sum_fifth_lambda():
    return list(filter(lambda x: x>50, map(lambda x: x**2, range(11))))

sum_fifth_lambda()

# List Comprehension
def sum_fifth_list():
    return [
        i**2
        for i
        in range(11)
        if i**2>50
    ]

sum_fifth_list()


# ## reduce

# In[12]:

# get_sum
# list의 값을 모두 더해 return
from functools import reduce


def get_sum(arr):
    res=0
    for i in arr:
        res+=i
    return res

reduce(lambda x, y: x+y, range(5))


# In[21]:

# get_max
# list의 최대값을 return

def get_max(arr):
    res=arr[0]
    for i in arr:
        if i > res:
            res = i;
    return res

reduce(lambda x, y: x if (x>y) else y, [1,2,3,-4])


# In[58]:

# get_avg
# [{}] 형태의 list를 입력받아 각각의 평균을 계산

data=[
    {"rent" : 50,
     "deposit" : 1000
    },
    {"rent" : 55,
     "deposit" : 2000
    },
    {"rent" : 60,
     "deposit" : 6000
    },
]


# In[53]:

def get_avg(data):
    res={}
    rent_sum=0
    dep_sum=0
    
    for i in data:
        rent_sum+=i["rent"]
        dep_sum+=i["deposit"]
    res["rent"]=rent_sum/3
    res["deposit"]=dep_sum/3
    
    return res

get_avg(data)


# In[54]:

#reduce(lambda x, y: x["rent"]+y["rent"], data)

# 위 연산은 {"rent" : 50, "deposit" : 1000} + {"rent" : 55, "deposit": 2000}의 연산
# 즉 dic인 x와 y가 통째로 들어와 연산됨.
# 두 번째 연산은 첫 번째 연산의 결과로 만들어진 dic이 적용됨
# 즉 {"rent":105} + {"rent":60, "deposit":6000}
# x["rent"]=105 + y["rent"]=60 이 연산됨
# 그렇기 때문에 x["rent"] + y["rent"]는 
# {"rent" : 50, "deposit" : 1000} + {"rent" : 55, "deposit": 2000}이 계산되어
# 두 번째 연산 시 x=105, 즉 105["rent"]를 찾는 꼴이 되어 연산에 실패한다

res=reduce(lambda x, y: {"rent" : x["rent"]+y["rent"],
       "deposit" : x["deposit"]+y["deposit"]}
       , data)


# In[55]:

for i in res:
    res[i]=res[i]/3
res


# In[62]:

rent_avg=(reduce(lambda x, y: x + y, [
        i["rent"]
        for i 
        in data
    ]))/3

rent_avg


# # 2. \*args, \**kwagrs

# In[70]:

# packing과 unpacking의 개념

def test(*args, **kwargs): # *args는 tuple로 가변 parameter를 packing
    print(args)            # **kwargs는 dic으로 가변 parameter를 packing
    print(kwargs)                       
    


# In[95]:

data=[1,2,3,4]
#test(("test", "tes1"), ("Test2", "test3"), ok="ok")
test(data)
test(*data) #unpacking


# In[98]:

# dic의 경우 unpack이 필요 없는 구조인듯?
test2(("test", "test1"), ("test2", "test3"),test="ok", name="power")


# ## 3. 응용

# In[112]:

def get_args_list(n, *args):
    arr=[];
    
    for i in range(n):
        text=""
        for ind, val in args:
            
            text+=val if (i+1)%ind==0 else ""
        arr.append(text);
        
    return arr


# In[113]:

get_args_list(10, (3, "fast"), (5, "test"), (7, "ok"))


# In[116]:

def get_args_lambda(n, *args):
    return list(map(
            lambda x: "".join(
            map(lambda y: y[1] if (x+1)%y[0]==0 else ""
                ,args)
            )
            , range(n)))


# In[118]:

get_args_lambda(10, (3, "fast"), (5, "test"), (7, "ok"))


# In[119]:

def get_args_test(n, *args):
    return [
        "".join([
                val if (i+1)%ind==0 else ""
                for ind, val in args                
            ])
        for i in range(n)
    ]


# In[120]:

get_args_test(10, (3, "fast"), (5, "test"), (7, "ok"))

