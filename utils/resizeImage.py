import cv2
from PIL import Image
from constants import *

im = Image.open("./images/shape0.jpg")
w, h = im.size

im_resized = im.resize((w, h), Image.ANTIALIAS)
im_resized.save("./images/shape0Resized.png", "PNG")
