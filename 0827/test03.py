'''
Created on 2017年8月27日

@author: Lin Yu
'''
class Parent:   #定义父类
    def myMethod(self):
        print('调用父类方法')
        
class Child(Parent):
    def myMethod(self):
        print('调用子类方法')
        
c = Child()
c.myMethod()