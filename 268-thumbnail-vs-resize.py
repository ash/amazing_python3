# Thumbnail vs resize

from PIL import Image

img = Image.open('landscape.jpg')
# width > height

size = (100, 100)
img2 = img.resize(size) # makes a copy
img.thumbnail(size) # changes in-place
img.save('landscape.thmb.jpg')
img2.save('landscape.rsz.jpg')

img.show()
img2.show()
