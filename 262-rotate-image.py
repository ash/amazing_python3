# Rotate an image

from PIL import Image

img = Image.open('bird.png')

img2 = img.rotate(30) # degrees
img2.show()
