import sys
from PIL import Image

img=Image.open(sys.argv[1]) 

img = img.resize((192, 108), Image.NEAREST)
img.save(sys.argv[2])
