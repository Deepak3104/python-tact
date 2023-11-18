import cv2 
'''import PIL
from PIL import Image'''

filepath = "/home/deepak/Downloads/p1.png"
image = cv2.imread(filepath) 
height, width = image.shape[:2] 
print(height,width)

'''image = Image.open('/home/deepak/Downloads/p1.png')
exifData = image._getexif()
print('exifData = ' + str(exifData))'''