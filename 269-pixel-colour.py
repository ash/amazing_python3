# What is the colour of a pixel?

from PIL import Image

img = Image.open('bird.png')
pixels = img.load()

clr = pixels[10, 10] # coords
# access as an matrix

print(clr)

# Also see the types:
print(type(pixels))
print(type(clr))