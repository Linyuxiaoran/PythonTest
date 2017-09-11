'''
Created on 2017年9月11日
输入描述:输入包括一个整数n,(1 ≤ n ≤ 10^5)
输出描述:输出一个整数,表示n的相反数
@author: Lin Yu
'''

x = input("请输入：")
list1 = []
for x1 in reversed(x):
    list1.append(x1)
    
print(int(x)+int(''.join(list1)))

