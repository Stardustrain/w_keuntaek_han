
# coding: utf-8

# In[26]:

animals=["dog", 
         "cat", 
         "fish", 
         "monkey", 
         "dog", 
         "dog",]; # multiline init 시 마지막 index는 ,를 붙여준다

print(animals[::-1]);


# In[46]:

import numpy as np;

a=np.arange(5, 10)

print(a)


# In[39]:

s_animals=set(animals);
print(s_animals);


# In[52]:

t_animals=tuple(animals);
print(t_animals);

a, b=(100, 200);
print(a);
print(b);


# In[53]:

student={"name" : "han", "age" : 30};
student["email"]="kthanterran@naver.com";
print(student)


# In[55]:

for _ in range(10):
    print("hello");


# In[66]:

for x in range(len(animals)):a
    print(animals[x]);
print("===============");
for x in animals:
    print(x);


# In[72]:

for x in student:
    print(x +" => "+str(student[x]));
    
print("==================");

for x, y in student.items():
    print(x+" => "+str(y));
    


# In[74]:

data=[["Han", "kthanterran@naver.com", "010-1111-1111"], 
     ["Lee", "kthanterran@daum.net", "010-2222-2222"], 
     ["Park", "kthanterran@gmail.com", "010-3333-3333"],];


# In[79]:

data_d={};
cnt=1;
for i in data:
    dic={};
    dic["name"]=i[0];
    dic["Email"]=i[1];
    dic["Phonenumber"]=i[2];
    data_d[cnt]=dic;
    cnt+=1;
print(data_d)


# In[92]:

data_d={};

for ind, i in enumerate(data):
    dic={};
    dic["name"]=i[0];
    dic["Email"]=i[1];
    dic["Phonenumber"]=i[2];
    data_d[ind+1]=dic;
    
data_d


# In[90]:

my_num=20

if my_num > 0:
    print("양수")
elif my_num==0:
    print("0")
else:
    print("음수")

