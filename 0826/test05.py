'''
Created on 2017年8月26日

@author: Lin Yu
'''
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()