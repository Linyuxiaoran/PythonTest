'''
Created on 2017年8月31日
将图片转化成字符画  参考http://blog.csdn.net/Richie_ll/article/details/69206210
@author: Lin Yu
'''
from PIL import Image 
#要索引的字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
img = Image.open("test02.jpg") #读取图像文件
(width,height) = img.size
img = img.resize((int(width*0.7),int(height*0.4))) #修改图像的大小比例
print(img.size)  #在控制台输出图片的大小

def convert(img):
    img = img.convert("L")  #转为灰度图像
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))  #获取每个坐标像素点的灰度
            unit = 256.0 / length 
            txt += ascii_char[int(gray / unit)]
        txt +='\n'
    return txt

txt = convert(img)
f = open("test02.txt","w") #保存到相对路径，请用txt文本打开，格式-字体-将字号设为2
#f = open(r"D:\DataSave\test02.txt","w") #保存到绝对路径
f.write(txt)  #储存到文件中
f.close() 