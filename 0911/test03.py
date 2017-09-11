'''
Created on 2017年9月11日
一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。
牛牛现在给定一个字符串,请你帮助计算这个字符串的所有碎片的平均长度是多少。
@author: Lin Yu
'''
s = input()
list1 = list(s)
lenth = len(list1)
cout = 1

for x in range(0,lenth-1):
    if list1[x]!=list1[(x+1)]:
        cout += 1

    
x1 = lenth / cout
print("%.2lf" %x1 )