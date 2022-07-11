import os
from PIL import Image # pip install Pillow
import pillow_avif # pip install pillow-avif-plugin

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def BtoMb(address):
    return toFixed((os.path.getsize(address)/pow(1024,2)),2)

def cutting(image):
    (width, height) = image.size
    return image.crop((0, 0, height, height))


address = input("image path [/Users/v.syroiezhin/Desktop/image_conversion/image.jpg]:")
image = Image.open(address)
image = cutting(image) # cut out the square (comment out if not needed)
output = input("choose the format to convert [webp,jpeg,avif,png]:")
image.convert("RGB").save(f"image.{output}", output)
print( BtoMb(address) , " ⮕ ", BtoMb(f'image.{output}') )