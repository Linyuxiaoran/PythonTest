'''
Created on 2017年8月30日
练习捕获百度登录验证码图片 方法1
@author: Lin Yu
'''
import urllib.request
import time

def saveFile(data,num):
    save_path = r'D:\DataSave\passport\image'+str(num)+'.png' #定义图片名称，保存在passport
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

count = 20
num = 1
while num<=count:
    weburl = 'https://passport.baidu.com/cgi-bin/genimage?tcGfb07c19ddf1ac1c102cc14f34401fd3106ec4307e4047f96'
    req = urllib.request.Request(url=weburl) #构建请求
    webPage = urllib.request.urlopen(req) #获取服务器相应
    data = webPage.read()
    saveFile(data,num)
    print('下载%d完成' %num)
    time.sleep(0.2) #限定一下速度
    num +=1