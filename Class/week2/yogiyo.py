
# coding: utf-8

# In[36]:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
get_ipython().magic('matplotlib inline')


# In[7]:

#1. response.json()
#2. postman > Generate Code

response = requests.get(
    "https://www.yogiyo.co.kr/api/v1/restaurants-geo/?items=20&order=rank&page=0&search=&zip_code=441390",
    headers={
        "X-ApiKey" : "iphoneap",
        "X-ApiSecret" : "fe5183cc3dea12bd0ce299cf110a75a2"
    }

)


# In[13]:

yogiyo = json.loads(response.text)
df = pd.DataFrame(yogiyo.get("restaurants"))
df.to_csv("yogiyo.csv")


# In[14]:

# 직방


# In[26]:

response=requests.get(
    "https://api.zigbang.com/v1/items?detail=true&item_ids=5915926&item_ids=5895583&item_ids=5899242&item_ids=5911969&item_ids=5908147&item_ids=5890852&item_ids=5990311&item_ids=5800896&item_ids=5845695&item_ids=5806587&item_ids=5970119&item_ids=5913209&item_ids=5813289&item_ids=5804386&item_ids=5870319&item_ids=5463938&item_ids=5856787&item_ids=5790062&item_ids=5952809&item_ids=5959810&item_ids=5937143&item_ids=5924839&item_ids=5975599&item_ids=5872702&item_ids=5836431&item_ids=5944050&item_ids=5968477&item_ids=5971402&item_ids=5914205&item_ids=5977584&item_ids=5975287&item_ids=5955586&item_ids=5930920&item_ids=5957730&item_ids=5937547&item_ids=5815690&item_ids=5950615&item_ids=5994222&item_ids=5933508&item_ids=5921091&item_ids=5914835&item_ids=5863610&item_ids=5996752&item_ids=5907239&item_ids=5972658&item_ids=5382608&item_ids=5895547&item_ids=5916397&item_ids=5909452&item_ids=5291509&item_ids=5837834&item_ids=5824708&item_ids=5853273&item_ids=5811866&item_ids=5984552&item_ids=5950348&item_ids=5982421&item_ids=5847479&item_ids=5848406&item_ids=5954893"
)

response2=requests.get(
    "https://api.zigbang.com/v1/items?detail=true&item_ids=5872856&item_ids=5995967&item_ids=5927094&item_ids=5933442&item_ids=5846538&item_ids=5820143&item_ids=5885239&item_ids=5889599&item_ids=5972686&item_ids=5820008&item_ids=5885245&item_ids=5902938&item_ids=5817427&item_ids=5841377&item_ids=5929721&item_ids=5875118&item_ids=5939937"
    )


# In[27]:

data1=pd.DataFrame([
        item.get("item")
        for item
        in response.json().get("items")
    ])

data2=pd.DataFrame([
        item.get("item")
        for item
        in response2.json().get("items")
    ])


# In[28]:

data1_df=data1[["id", "deposit", "rent"]]
data2_df=data2[["id", "deposit", "rent"]]


# In[37]:

data1_df.plot.scatter(x="deposit", y="rent", color="red")


# In[39]:

data2_df.plot.scatter(x="deposit", y="rent", color="blue")


# In[40]:

# 웹서비스에서는 비추 > 리소스 문제 + 복잡한 구현 방식


# In[41]:

# 히스토그램 :: JSON API를 만들어서
# javascript로 시각화 :: d3.js, highchart
# 파이썬 => seaborn . bokeh


# In[ ]:

# awesome-python  / awesome-django  / trending(python 부분) < github에 문서화되어 정리되어 있음
# pytest, unittest

