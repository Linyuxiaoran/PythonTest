'''
Created on 2017年9月1日
创建四位数的验证码
@author: Lin Yu
'''
from PIL import Image,ImageDraw,ImageFont#,ImageFilter #若需要模糊化处理，则应引入此包。 
import random
#产生随机验证码内容
def rndTxt():
    txt = []
    txt.append(random.randint(97,123))  #大写字母
    txt.append(random.randint(65,90))  #小写字母
    txt.append(random.randint(48,57)) #数字
    print(txt)
    x1 = chr(txt[random.randint(0,2)])
    print(x1)
    return x1   #为验证产生的内容，特设置变量获取chr(txt[random.randint(0,2)])的值。正规写法如下
    #return chr(txt[random.randint(0,2)])

#随机颜色（背景）
def rndColor():
    return(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#随机颜色（字体）
def rndColor2():
    return(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240*60
width = 60*4
height = 60
img = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype(u'shiguang.ttf', 36)
draw = ImageDraw.Draw(img)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
                
#输出文字
for txt in range(4):
    draw.text((60*txt+10,10),rndTxt(),font=font,fill=rndColor2())
#模糊化处理
#img = img.filter(ImageFilter.BLUR)

img.save("test03-1.jpg")
print("完成")