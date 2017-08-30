'''
Created on 2017年8月30日
练习捕获百度登录验证码图片 方法2
@author: Lin Yu
'''
import time
import urllib.request

def get_image(url,num):
    request = urllib.request.Request(url) #构建请求
    response = urllib.request.urlopen(request) #获取服务器相应
    get_img = response.read()
    fileName = r'D:\DataSave\passport1\image'+str(num)+'.png' #定义图片名称，保存在passport1
    with open(fileName,'wb')as fp:  #貌似用with open 不用写close之类的东西？
        fp.write(get_img)
        print('图片%d下载完成' %num)  #获取控制台输出
    return 

count = 20 #定义循环次数
num = 1 #定义开始值
while num<=20:
    url = 'https://passport.baidu.com/cgi-bin/genimage?tcGfb07c19ddf1ac1c102cc14f34401fd3106ec4307e4047f96' #URL地址
    get_image(url,num)
    time.sleep(1) #限定一下速度
    num +=1