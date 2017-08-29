'''
Created on 2017年8月29日
http://118.89.198.225/wp-content/uploads/2017/06/cematongyou.jpg
@author: Lin Yu
'''
import urllib
import urllib.request

def get_image(url):
    request = urllib.request.Request(url) #构建请求
    response = urllib.request.urlopen(request) #获取服务器相应
    get_img = response.read()
    with open('001.jpg','wb')as fp:
        fp.write(get_img)
        print('图片下载完成')
    return 
url = 'http://118.89.198.225/wp-content/uploads/2017/06/cematongyou.jpg'
get_image(url)