# 图片库
import hashlib

from PIL import Image
# 绘画库
from PIL import ImageDraw
# 字体库
from PIL import ImageFont
# 导入随机库
import random


# 构建图片验证码
def draw_code_img():
    # 设定宽高
    width = 120
    height = 60

    # 构建画布
    img = Image.new("RGB", (width, height), "white")
    # 构建画笔
    draw = ImageDraw.Draw(img)
    # 定义字体
    font = ImageFont.truetype(font=r"C:\Users\dell\Desktop\my_project\django+vue\my_django\static\code\my_font.TTF",
                              size=40)
    # 设置随机背景颜色
    for x in range(width):
        for y in range(height):
            draw.point((x, y), (random.randint(64, 164), random.randint(64, 164), random.randint(64, 164)))
    # 接收验证码
    msg = ""
    for i in range(4):
        # 定义显示文字
        text = chr(random.randint(65, 90))
        # 文字颜色
        text_color = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
        # 开始作画
        draw.text((10 + i * 20, 10), text=text, fill=text_color, font=font)
        # 接收验证码
        msg += text
    img.save(r"C:\Users\dell\Desktop\my_project\django+vue\my_django\static\code\code.png", "png")
    return msg


# MD5加密方法
def make_password(mypass):
    #生成md5对象
    md5 = hashlib.md5()
    # 为了安全起见 ，转码
    mypass = str(mypass).encode(encoding="utf-8")
    # 加密操作
    md5.update(mypass)
    # 生成密文
    password = md5.hexdigest()
    # 返回密文
    return password