'''
Created on 2017年8月27日

@author: Lin Yu
'''
#类定义
class people:
    name = ''
    age = 0
    #定义私有属性
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a 
        self.__weight = w 
    def speak(self):
        print("%s 说，我%d岁" %(self.name,self.age))
        
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g 
    #覆盖父类的方法
    def speak(self):
        print("%s 说，我 %d 岁了， 我在读 %d 年级" %(self.name,self.age,self.grade))
        
#另一个类，多重继承的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n 
        self.topic = t 
    def speak(self):
        print("我叫%s， 我是一个演说家，演讲的主题是 %s" %(self.name,self.topic))
    
#多重继承
class sample(student,speaker):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)
        
test = sample("Tim",25,80,4,"python")
test.speak() #    方法名同，默认调用的是在括号中排前地父类的方法
        
        
        
        
        
        
        
        
        
        
        
        
        
        