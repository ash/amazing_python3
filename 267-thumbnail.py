# How to create a thumbnail
# from an image

from PIL import Image

img = Image.open('bird.png')
img.thumbnail((100, 100)) # tuple
img.save('bird.small.png')

# Just to see it
img.show()
