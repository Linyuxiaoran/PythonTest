'''
Created on 2017年8月30日
保存爬取回来的报文
@author: Lin Yu
'''
def saveFile(data):
    save_path = r'D:\DataSave\temp.out' #示例里没有那个'r',运行时产生报错OSError: [Errno 22] Invalid argument
    f_obj = open(save_path, 'wb') #wb 表示打开方式
    f_obj.write(data)
    f_obj.close()

data = '' #此代码为防止编译器报错，使用时请删去此行。
#这里省略爬虫代码
#......

#爬到的数据保存在 data变量里
#将data变量保存到D盘下
saveFile(data)