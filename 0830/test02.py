'''
Created on 2017年8月30日
一个简单的爬虫示例2
@author: Lin Yu
'''
import urllib.request

def saveFile(data):
    save_path = r'D:\DataSave\temp.out'  #示例里没有那个'r',运行时产生报错OSError: [Errno 22] Invalid argument
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

weburl = 'http://118.89.198.225/?page_id=2'
webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
webheader2 = {
    'Connection':'Keep-Alive',
    'Accept':'text/html, application/xhtml+xml, */*',
    'Accept-Language':'en-US,en;q=0.8,zh_Hans_CN;q=0.5,zh_Hans;q=0.3',
    'User-Agent':'Mozilla/5.0(Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    #'Accept-Encoding': 'gzip, deflate',
    'Host':'118.89.198.225',
    'DNT': '1'
    }

req = urllib.request.Request(url=weburl, headers=webheader2)
webPage = urllib.request.urlopen(req)
data = webPage.read()
saveFile(data) #将data变量保存到D盘下
data = data.decode('UTF-8')
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
