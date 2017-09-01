'''
Created on 2017年8月31日
地下城堡2计算资源何时满仓
@author: Lin Yu
'''
import time  
import math  
          
def changeTime(allTime):   #引入时间转换函数
    day = 24*60*60  
    hour = 60*60  
    min = 60  
    if allTime <60:          
        return  "%d sec"%math.ceil(allTime)  
    elif  allTime > day:  
        days = divmod(allTime,day)   
        return "%d days, %s"%(int(days[0]),changeTime(days[1]))  
    elif allTime > hour:  
        hours = divmod(allTime,hour)  
        return '%d hours, %s'%(int(hours[0]),changeTime(hours[1]))  
    else:  
        mins = divmod(allTime,min)  
        return "%d mins, %d sec"%(int(mins[0]),math.ceil(mins[1]))  
    
    
def start():
    #sum = input("资源总数")  #资源总数
    round1 = input("流水线周期是：") #流水线时间
    get1 = input("生产效率是：")  #一次获得的数量
    total =input("资源上限是：")  #资源上限
    now = input("目前资源量是：")  #目前资源数量
    x1 = (int(total) - int(now))// int(get1) #获取流水线循环次数
    seconds = x1 * int(round1) 
    
    return int(seconds)

if __name__=="__main__":  
    seconds = start()
    data = changeTime(int(seconds))  
    print ("距离满仓时间为：" + data)
    
    