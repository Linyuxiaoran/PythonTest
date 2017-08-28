'''
Created on 2017年8月28日
匹配实例1
@author: Lin Yu
'''
import re 
print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))