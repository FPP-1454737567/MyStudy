"""
@Time  : 2024/3/4
@Author: panpan.fang@shopee.com
@File  : gegerateImage.py
@IDE   : PyCharm
"""
from PIL import Image

# 创建一个新的图片对象，大小为1200x240，背景色为黑色（RGB值为(0,0,0)）
img = Image.new('RGB', (1200, 240), color=(0, 0, 0))

# 保存图片
img.save('my_image.png')