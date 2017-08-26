'''
Created on 2017年8月26日

@author: Lin Yu
'''
class Complex:
    def __init__(self,  realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)