from PIL import Image, ImageEnhance
import math

inPng = "subject.png"
outPng = "edi2.png"

im = Image.open(inPng).convert('L')
px = im.load()

width, height = im.size

for row in range(0,height):
  for col in range (0, width):
    print ("%03d" %px[col, row], end="")
  print("")
     

