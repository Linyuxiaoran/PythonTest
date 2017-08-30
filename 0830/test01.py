'''
Created on 2017年8月30日
一个简单的爬虫示例1
@author: Lin Yu
'''
import urllib.request
url = 'http://118.89.198.225/?page_id=2'
webPage = urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')
#print(data)
print("type(webPage)是")
print(type(webPage))
print()
print("webPage.geturl()是")
print(webPage.geturl())
print()
print("webPage.info()是")
print(webPage.info())
print()
print("webPage.getcode()是")
print(webPage.getcode())
