
# coding: utf-8

# ## 1. Class Basic

# In[1]:

class Shape():
    def __init__(self, width, heigth):
        self.width=width
        self.heigth=heigth
        
    def area(self):
        print(self)
        
    def is_bigger_than(self, another):
        if not isinstance(another, Shape):
            return "error"
        return self.area() > another.area()

class Triangle(Shape):
    def area(self):
        return (self.width * self.heigth) / 2
    
class Square(Shape):
    def area(self):
        return self.width * self.heigth


# In[3]:

t1=Triangle(3, 4)
s1=Square(3, 4)

# 클래스 타입 체크
print(type(t1) is Triangle)
print(isinstance(t1, Shape))

# 상속 여부
# 비교하고 싶은 클래스를 tuple로 한꺼번에 넣을 수 있음
print(issubclass(Triangle, Shape))

t1.is_bigger_than(s1)


# In[5]:

# 이런 것도 가능 함
for shape in [t1, s1]:
    print(shape.area())


# ## 2. class method의 종류

# In[23]:

class Test(object):
    
    data="class data"; # class 전체가 공유하는 값.
                       #  intance생성시 값 수정이 없으면 그대로 상속함
    def __init__(self, data):
        self.data = data   # instance data에 접근
    
    
    def instance_method(self):
        return self.data
    
    @classmethod
    def class_method(cls):
        return cls.data  # class data에 접근
    
    @staticmethod
    def static_method():
        return "static!"


# In[24]:

c=Test("data")


# In[25]:

c.instance_method()


# In[26]:

Test.class_method()
# c.class_method() 인스턴스에서도 클래스메소드 호출이 가능함


# In[29]:

c.static_method()
Test.static_method()


# ## 3. Decorator 실전

# In[30]:

# login_required
# is_admin


# In[4]:

class User():
    def __init__(self, user, is_admin=False):
        self.user = user
        self.is_admin = is_admin
        
class Request():
    def __init__(self, url, user=None):
        self.url = url
        self.user = user
        
class Response():
    def __init__(self, body):
        self.body = body
        
    def __repr__(self):
        return "Response : {body}".format(body=self.body)


# In[5]:

def mypage(request):
    if request.user :
        res = Response("{name} 정상 접속".format(name=request.user.user))
    else :
        res = Response("로그인 필요")
        
    return res


# In[4]:

user=User("Han")
admin=User("admin", is_admin=True)
request=Request("/index/", user)
mypage(request)


# In[5]:

# Decorator 만들기


# In[9]:

def login_required(func):
    print("login war")
    def wrapper(request, *args, **kwargs):
        print("login")        
        #print(is_admin)
        if request.user:
            return func(request, *args, **kwargs)
        else :
            res = Response("로그인 필요")
            return res
    return wrapper


# In[10]:

def is_admin(func):
    print("admin war")
    def wrapper(request, *args, **kwargs):
        print("admin")
        if request.user and request.user.is_admin:
            return func(request, *args, **kwargs)
        else:
            res = Response("접근권한 없음")
            return res
    return wrapper


# In[11]:

@login_required
def secondpage(request):
    print("call!")
    return "{name} 정상 접속".format(name = request.user.user)


# In[12]:

@login_required
@is_admin
def adminpage(request):
    print("call!!!")
    return "{name} 접속".format(name=request.user.user)


# In[14]:

request=Request("/index/")
adminpage(request)


# In[26]:

adminrequest=Request("/admin/")
adminpage(adminrequest)


# In[1]:

@login_required
@is_admin
def adminpage(request):
    print("call!!!")
    return "{name} 접속".format(name=request.user.user)


# In[3]:

adminrequest=Request("/admin/")
adminpage(adminrequest)


# In[15]:

def test(*args, **kwargs):
    print(*args)
    print(*kwargs)
    
test(1,2,3,(4,5), key="test", test1="Test2")


# In[34]:

def start(func):
    def wrapper():
        print("statrt")
        func()
    return wrapper


# In[35]:

def end(func):
    def wrapper():
        print("end")
        func()

    return wrapper


# In[36]:

@end
@start
def hello():
    print("hello")


# In[37]:

hello()


# In[ ]:



