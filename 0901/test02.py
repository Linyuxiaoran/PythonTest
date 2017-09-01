'''
Created on 2017年9月1日
给图片加上数字
@author: Lin Yu
'''
#draw.text((width-28,-8),'1',font=myfont,fill='white')

from PIL import Image, ImageDraw, ImageFont
img = Image.open("test02.jpg")
draw = ImageDraw.Draw(img)
myFont = ImageFont.truetype(u"shiguang.ttf", 50)
(width,height) = img.size
draw.ellipse((width-40,0, width,40),fill="red",outline="red") #在图上画一个圆
draw.text((width-28,-8),'1',font=myFont,fill = 'white')
img.save('test02-1.jpg')
print("完成")