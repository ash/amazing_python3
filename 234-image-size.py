# What are the width and height
# of an image?

from PIL import Image

image = Image.open('bird.png')
width, height = image.size

print(f'{width}x{height} pixels')