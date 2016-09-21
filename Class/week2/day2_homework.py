
# coding: utf-8

# In[1]:

'''
def cont_matrix(n):
    sub_arr=[];
    arr=[];
    for i in range(1, n*n+1):            
        if i%n==0:
            sub_arr.append(0)
            arr.append(sub_arr)
            sub_arr=[];
        else:
            sub_arr.append(0)
           
    return arr
'''
from numpy import zeros


def snail(n):
    #mat=cont_matrix(n)
    mat=zeros((n, n))
    limit=n
    flag=1
    num=1
    x=0
    y=-1
    
    while True:
        for i in range(limit):
            y+=flag
            mat[x][y]=num
            num+=1
        
        limit-=1
        
        if limit == 0: break;
        
        for i in range(limit):
            x+=flag
            mat[x][y]=num
            num+=1
        
        flag=-flag
    
    return mat

snail(6)


# In[2]:

def get_awesome_list(n, *args):
    return [
        "".join([
                text if (i+1) % ind == 0 else ""
                for ind, text
                in args
            ])
        for i
        in range(n)
    ]

get_awesome_list(10, (3, "ok"), (5, "test"), (7, "good"))


# In[4]:

def get_awesome_lambda(n, *args):
    return list(map(
            lambda y: "".join(map(
                lambda x: x[1] if (y+1)%x[0]==0 else ""
                ,args))
            , range(n)))

get_awesome_lambda(10, (3, "ok"), (5, "test"), (7, "good"))

