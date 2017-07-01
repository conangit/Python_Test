
from PIL import Image

im = Image.open('test.png')
print(im.format, im.size, im.mode)

im.thumbnail((500,300))
im.save('thumb.jpg', 'JPEG')