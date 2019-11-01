from PIL import Image, ImageDraw, ImageFont

import Adafruit_SSD1306

RST = None

DISP_ADDR = 0x3c

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

disp.clear()

disp.display()

size = disp.width, disp.height

font = ImageFont.truetype('msyh.ttc', 12)

image = Image.new('1', size)

draw = ImageDraw.Draw(image)

draw.text((0, 0), '古诗一首', font=font, fill=255)

draw.text((0, 20), '白日依山尽, 黄河入海流', font=font, fill=255)

draw.text((0, 38), '欲穷千里目, 更上一层楼', font=font, fill=255)

disp.image(image)

disp.display()