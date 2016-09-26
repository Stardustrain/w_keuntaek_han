
# coding: utf-8

# ## 크룰링

# In[1]:

# requests 외부 모듈 사용
# 사실상의 표준 (de facto)


# In[4]:

import requests


# In[5]:

response=requests.get("http://www.naver.com")


# In[6]:

response


# In[8]:

response.text


# In[9]:

# "realrank"라는 id를 가진 ol태그
# 그 안의 "li" 10개


# In[11]:

from bs4 import BeautifulSoup


# In[12]:

res=BeautifulSoup(response.text, "html.parser")


# In[13]:

elements=res.select("ol#realrank li")


# In[15]:

len(elements)


# In[19]:

arr=[]
for i in elements:
    arr.append(i.select_one("a").attrs["title"])


# In[21]:

arr


# In[23]:

[
    i.select_one("a").attrs["title"]
    for i in elements
]

