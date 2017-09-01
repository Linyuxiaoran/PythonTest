'''
Created on 2017年8月31日

@author: Lin Yu
'''
from PIL import Image,ImageDraw,ImageFont

#http://font.chinaz.com/zhongwenziti.html 字体下载网站

img = Image.open('test03.jpg')
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('HYLiuZiHeiJ.ttf',size=80)
fillcolor = 'pink'
(width, height) = img.size
#第一个参数是加入字体的坐标
#第二个参数是文字内容
#第三个参数是字体格式
#第四个参数是字体颜色
draw.text((40,100),u'萌萌哒',font=myfont,fill=fillcolor)
img.save('test03-1.jpg')
print("完成")