import time
import sys
import pyocr
import pyocr.builders
from PIL import Image

imgX = 32
imgY = 346
cropW = 940
cropH = 50

im = Image.open("./txt.png")
box = (imgX, imgY, imgX + cropW, imgY + cropH)
im = im.crop(box)
im.save("crop.png")
