
# coding: utf-8

# In[15]:

import requests
from bs4 import BeautifulSoup


# In[16]:

# 네이버블로그 검색 결과
# ul#elThumbnailResultArea li.sh_bolg_top

response=requests.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=python")
response


# In[17]:

res=BeautifulSoup(response.text, "html.parser")


# In[18]:

elemsnts=res.select("ul#elThumbnailResultArea li.sh_blog_top")


# In[19]:

len(elemsnts)


# In[20]:

# [비정상적인 요청] 응답에 대한 우회
# 1. server ip 변경
# 2. 초당 request 회수 > 기다림
# 3. requests.get > header / user-agent에 모듈 정보가 노출 > 변경하여 접속


# In[34]:

# user-agent 변경, 우회
# Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10
IPAD_USER_AGENT = "Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10"

response=requests.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=python",
headers={"User-Agent":IPAD_USER_AGENT})


# In[35]:

bs=BeautifulSoup(response.text, "html.parser")
post_elements=bs.select("ul#addParemt li.api_bx") # 
#chrome user-agent switcher


# In[38]:

data="\n".join([
    elem.select_one("div.total_tit").text
    for elem
    in post_elements
])
#post_elements.select_one("div.total_tit").text


# In[40]:

data


# In[129]:

# 여러 페이지결과를 CSV로 저장
# 함수, (키워드 , 페이지 수)

def url_listing(keyword, page):
    #arr=[]
    
    arr=[
        "http://search.daum.net/search?w=blog&m=board&collName=blog_total&q="+keyword+"&spacing=0&DA=PGD&page="+str(i)
        for i
        in range(1, page+1)
    ]
    #for i in range(1, page+1):
    #    arr.append("http://search.daum.net/search?w=blog&m=board&collName=blog_total&q="+keyword+"&spacing=0&DA=PGD&page="+str(i))
    return arr


# In[152]:

def page_parsing(url):
    response=requests.get(url)
    bs=BeautifulSoup(response.text, "html.parser")
    post_elem=bs.select("ul#blogResultUl li")
    
    # dic 꿀팁
    # dic에는 .get()이라는 것이 있음!
    # dic에 key값이 name, email이 있는 경우
    # dic["addr"]을 하면 error가 발생한다
    # 이 때 dic.get("addr")을 하면 None값을 반환하며, 
    # dic.get("addr", "Default")로 default값 설정도 가능하다
    
    
    result=[
        {
            "title" : elem.select_one("div.wrap_cont div.cont_inner div.wrap_tit").text.replace("\n", ""),
            "url" : elem.select_one("div.wrap_cont div.cont_inner div.info span a").text,
            "blog_title" : elem.select_one("div.wrap_cont div.cont_inner div.info span a.f_nb").text
        }
        for elem
        in post_elem

    ]
    
  
    '''
    result=[]
    for elem in post_elem:
        dic_data={}
        dic_data["title"]=elem.select_one("div.wrap_cont div.cont_inner div.wrap_tit").text.replace("\n", "")
        dic_data["url"]=elem.select_one("div.wrap_cont div.cont_inner div.info span a").text
        dic_data["blog_title"]=elem.select_one("div.wrap_cont div.cont_inner div.info span a.f_nb").text
        result.append(dic_data)
    '''
    return result
    


# In[156]:

def get_pages(keyword, page):
    page_list=[]
    #result=[] 
    page_list=url_listing(keyword, page)    
    
    '''
    for i in page_list:
        result.append(page_parsing(i))
    ''' 
    result = [
        page_parsing(i)
        for i
        in page_list
    ]
    
    posts=[]
    
    for i in range(len(result)):
        posts = posts + result[i]
    
    return posts
        


# In[158]:

get_pages("파이썬", 2)


# In[ ]:

# 직방, 요기요 static site 크룰링


# In[309]:

# 읽어온 html파일 내의 javascript를 브라우저가 실행!
# 기존의 방법으로는 정보를 모아올 수 없다

# 동적인 사이트
# ajax
# api
# javascript
# client rendering

# 즉 외부 API를 찾는 것이 핵심!

# google chrome web developer + jsonview << pugin으로 설치


# In[365]:

response = requests.get("https://api.zigbang.com/v1/items?detail=true&item_ids=5860311&item_ids=5963314&item_ids=5943359&item_ids=5887722&item_ids=5886742&item_ids=5909512&item_ids=5992321&item_ids=5910434&item_ids=5900804&item_ids=5861654&item_ids=5743924&item_ids=5834630&item_ids=5935234&item_ids=5972465&item_ids=5749419&item_ids=5993693&item_ids=5934880&item_ids=5858795&item_ids=5761530&item_ids=5884740&item_ids=5902192&item_ids=5993483&item_ids=5449860&item_ids=5908033&item_ids=5953164&item_ids=5945718&item_ids=5868300&item_ids=5981876&item_ids=5924879&item_ids=5990174&item_ids=5929972&item_ids=5946970&item_ids=5909416&item_ids=5970032&item_ids=5933984&item_ids=5935768&item_ids=5886735&item_ids=5975299&item_ids=5879868&item_ids=5937139&item_ids=5979781&item_ids=5928408&item_ids=5886011&item_ids=5875945&item_ids=5951430&item_ids=5768142&item_ids=5984101&item_ids=5825881&item_ids=5766165&item_ids=5875749&item_ids=5961944&item_ids=5972879&item_ids=5593527&item_ids=5891386&item_ids=5986822&item_ids=5825518&item_ids=5748899&item_ids=5953769&item_ids=5895924&item_ids=5991349")


# In[316]:

# response.text는 string 형태로 return 됨

import json

stud={"name" : "han", "mail":"test@nsm.net", "skiils" : ["python", "ruby"] }

stud_str = json.dumps(stud)   # input으로 dic, json을 받아서 output으로 json형태의 str을 return
stud_str                      # dump > 파일에 저장


# In[315]:

json.loads(stud_str)    # input은 json형태의 string을 받아 output은 python dic으로 바꿈


# In[366]:

zigbang = json.loads(response.text)


# In[350]:

#zigbang["items"][0]["item"]["deposit"]
#zigbang["items"][0]["item"]["rent"]

'''
[
    {
        "id" : zigbang["items"][i]["item"]["id"],
        "deposit" : zigbang["items"][i]["item"]["deposit"],
        "rent" : zigbang["items"][i]["item"]["rent"],
    }
    for i
    in range(len(zigbang["items"]))
]
'''

rooms = [
    {
        "room_id" : item.get("item").get("id"),
        "deposit" : item.get("item").get("deposit"),
        "rent" : item.get("item").get("rent"),
    }
    for item
    in zigbang.get("items")
]

# !! zigbang에 data가 안들어 왔을 경우?
# zigbang.get("items", [{"item":{}}]) <<< 오류를 줄이라!


# In[338]:

for i in rooms:
    "\n".join([
            "{room_id},{deposit},{rent}".format(
                room_id = room.get("room_id"),
                deposit = room.get("dsposit"),
                rent = room.get("rent"),
            )
            for room
            in rooms
        ])


# In[340]:


fp=open("zigbang.csv", "w")
fp.write("room_id,deposit,rent\n")
fp.write("\n".join([
            "{room_id},{deposit},{rent}".format(
                room_id = room.get("room_id"),
                deposit = room.get("dsposit"),
                rent = room.get("rent"),
            )
            for room
            in rooms
        ]))

fp.close()

# dataBase에 저장 (NoSQL 등...)
# zigbang.json으로 저장


# In[342]:

json.dump(
    zigbang, 
    open("zigbang.json", "w")
)


# In[343]:

# serialize, Deserialize
# pickle
# json => python 객체 <=> javascript 객체
# pickle => 객체 <=> binary
# 주로 datascience부분에서 dataFrame을 저장할 때나 클래스의 객체를 저장할 수도 있다

'''
import pickle

pickle.dump(
    stud, 
    open("sutd.pkl", "wb")
)
'''


# In[373]:

# pandas

import pandas as pd
from functools import reduce

df=pd.DataFrame(rooms)

# 월세 평균
# reduce
total=reduce(lambda a, b: {"rent":a["rent"]+b["rent"]}, rooms)
total["rent"] / len(rooms)
# pandas
df.rent.mean()

#df.to_csv("pd_zigbang.csv", index=False)

df1=pd.DataFrame(
    [
        item.get("item") for item in zigbang.get("items")
    ]
)
df1.head()


# In[374]:

df.describe()


# In[376]:

# 1. filtering
# row
df1.loc[0]
#column
df1.deposit


# In[380]:

# 2.
df1.deposit > 10000 # boolean Sereis(pd.Series) / Masking Table
df[df1.deposit > 10000][df1.rent >= 10]


# In[382]:

get_ipython().magic('matplotlib inline')

df.deposit.hist()


# In[386]:

student={"test":"OK"}

def get_addres(arr):
    return arr["address"]

try :
    get_address(student)
except:
    raise zigabngDataEmptyError("")


# In[384]:

# zigbang={}에 data가 없는 (empty)경우의 에러 발생

class zigabngDataEmptyError(Exception):
    def __init__(self, msg):
        self.msg=msg


# In[159]:

# iterator
# generator


# In[161]:

# iterable
# list, dic, tuple, set, string....


# In[163]:

# List는 iterator가 아님
# iterator는 내부적으로 __next__() 함수를 가짐


# In[189]:

animals=["dog", "cat", "fish"]


# In[190]:

for aninmal in animals:
    print(aninmal)


# In[191]:

# List객체에는 __iter__() 함수가 있음
# 즉 List.__iter__()를 호출하면 list_iterator 객체가 return


# In[185]:

animals_iter=animals.__iter__()


# In[186]:

animals_iter


# In[192]:

animals_iter.__next__()


# In[193]:

animals_iter.__next__()


# In[194]:

animals_iter.__next__()


# In[196]:

animals_iter.__next__()   # stopIteration error raise까지 출력됨
# iterator는 값을 next로 소비하고 나면 메모리에서 소거된다


# In[210]:

# 즉 for i in animals 는
# animals_iter = animals.__iter__()
# ===> list_iterator 객체를 return
# animals_iter.__next__() ==> 실제 값을 return
# 언제까지? StopIteration이 될 때 까지

# iterable >> iter() > iterator 객체가 return 되기를 expected하는 상황
# iterator >> next(iterator) > 변수가 나오다가 raise StopIteration()되기를 expected하는 상황

# list는 iterable하지만 iterator가 아니고
# list_iterator는 iterable과 동시에 iterator한 객체임


# In[211]:

data={"key":True, "key2":False}
data_iter=data.__iter__()
# data_iter=iter(data)
# data_iter=next(iter(data)) > 호출 시 마다 계속 data가 iter로 초기되어 맨 앞의 값만 출력


# In[212]:

data_iter.__next__()
# next(data_iter)


# In[213]:

# range class를 직접 만드는 것
# iter와 next가 있으니, 이 클래스는 iterable하면서 iterator한 class 임
class myrange():
    def __init__(self, n):
        self.i, self.n = 0, n
    
    def __iter__(self):    # iterable
        return self    # iterator
    
    def __next__(self):    # iterator
        if self.i < self.n:
            i=self.i
            self.i+=1
            return i
        else :
            raise StopIteration


# In[214]:

for i in myrange(5):     # iter(myrange(5)) >> __next__()
    print(i)


# In[216]:

# iterator이자 iterable한 객체의 문제?
# element들이 메모리에서 소거되기 때문에
# list와 dic은 재사용될 우려가 있어 iterable하지만 iterator는 아니다
# 그래서 for문에 진입시 원본 list를 따로 두고 iterator 객체가 따로 만들어 진다


# In[222]:

myr=list(myrange(5))
myr


# In[252]:

class myrange():
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        return myrange_iterator(self.n) # myrange의 iter가 호출 될 떄 마다 초기화 됨
                                        # 즉, 메모리에서 소거되지 않음  
class myrange_iterator():
    def __init__(self, n):
        self.i, self.n = 0, n
    
    def __iter__(self):    # iter가 여러번 호출 될 시 자기 자신을 return함
        return self        # e.g > iter(iter(myrange_iterator))
    
    def __next__(self):
        if self.i < self.n:
            i=self.i
            self.i+=1
            return i
        else :
            raise StopIteration()


# In[259]:

myr=myrange(5)
list(myr) # << list로 바뀔 시에도 iter()함수가 실행됨


# In[260]:

# Generator 
# iterator처럼 동작하는 객체를 생성시켜주는 함수
# 즉 함수의 결과값으로 iterator처럼 동작하는 객체를 return


# In[265]:

def myrange(n):    # myrange_iterator class 와 같은 개념
    i=0
    while i < n:
        #print("hello")
        yield i             # return => "yield"부분
        i+=1                # yield가 모두 소진되면 StopIter() 호출


# In[274]:

g_myr=myrange(3)


# In[273]:

next(g_myr)


# In[276]:

for i in myrange(5):
    print(i)


# In[280]:

# iterable?  > generator는 iterator이고, generator를 return하기 떄문에 iterable하다
iter(g_myr)

# iterator?
next(g_myr)


# In[281]:

class myrange:
    def __init__(self, n):
        self.n=n
        
    def __iter__(self):
        def myrange(n):    # myrange_iterator class 와 같은 개념
            i=0
            while i < n:
                #print("hello")
                yield i             # return => "yield"부분
                i+=1
        return myrange(self.n)      # generator는 객체라는 것을 잊지 말자!
                                    # 각자 상태값을 저장하고 있음


# In[282]:

myr=myrange(5)


# In[284]:

# Generator Comprehension
# [] 대신 ()를 해줌
# generator는 연산을 next시에만 수행함


# In[288]:

import time

def hard_function(username):
    print("FUCK")
    time.sleep(2)
    return username

data=["dog", "fish", "cat", "lion"]


# In[290]:

[
    hard_function(name)
    for name
    in data
]

# 모든 연산을 실행한 후 결과값 반환


# In[293]:

gen=(
    hard_function(name)
    for name
    in data
)

gen


# In[295]:

for i in gen:
    print(i)


# In[298]:

def gen_wrapper(data):
    for name in data:
        yield hard_function(name)
gen=gen_wrapper(data)


# In[299]:

# 함수형 프로그래밍의 기초!
# eval      > expression을 받는다
# exec      > statement를 받는다 (if, else, def, class 등....)
# expression and statement 검색


# In[300]:

eval("1+2")


# In[301]:

def hello():
    print("hello!")


# In[302]:

eval("hello()")


# In[306]:

for i in range(4):
    exec(
        "def multi_{number}(n) : print({number})".format(number=i)
    )


# In[308]:

multi_0(0)
multi_1(1)


# In[ ]:



