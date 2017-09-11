'''
Created on 2017年9月11日

@author: Lin Yu
'''
s = input()
list1 = list(s)
lenth = len(list1)
yuan = 1
sum1 = 0
for x in range(0,lenth-1):

    
    
        
    if list1[x]==list1[x+1]:
        
            
        yuan +=1
        if x==int(lenth-2):
            sum1 = sum1 + yuan
        print(yuan)

    if list1[x]!=list1[(x+1)]:
        if x==int(lenth-2):
            yuan += 1
            print(yuan)
        print("不等于" + str(yuan))
        sum1 = sum1 + yuan
        yuan = 1
    
    
        
        
        
print(list1)
print(sum1)