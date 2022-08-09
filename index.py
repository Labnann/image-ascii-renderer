from PIL import Image, ImageEnhance
import sys

image_file = sys.argv[1] 

im = Image.open(image_file).convert('L')
px = im.load()

width, height = im.size

def get_rendered_character(x):
    if (x in range (0, 25)):
      return ' '
    if (x in range (25, 50)):
      return '.'
    if (x in range (50, 75)):
      return ':'
    if (x in range (75, 100)):
      return '-'
    if (x in range (100,125)):
      return '+'
    if (x in range (125, 150)):
      return '*'
    if (x in range (150, 175)):
      return '='
    if (x in range (175, 200)):
      return '%'
    if (x in range (200,225)):
      return '@'
    if (x in range (225,255)):
      return '#'
   
    return 'O' 

def get_printformat (row, col):
  value = px[col, row]
  render = get_rendered_character(value)
  return render 

def get_printformat_num (row, col):
  value = px[col, row]
  return "%03d" %value 

for row in range(0,height):
  for col in range (0, width):
    print (get_printformat(row, col), end="")
  print("")
     
