import cv2 
from PIL import Image
import piexif

image1 = Image.open('/home/deepak/Downloads/p1.png')
exifData = image1._getexif()

if exifData is None:
    exifData = {}

filepath = "/home/deepak/Downloads/p1.png"
image = cv2.imread(filepath) 
height, width = image.shape[:2] 
print(height,width)

exifData['height'] = height
exifData['width'] = width
exifDataBytes = piexif.dump(exifData)

image1.save('image.jpg', format='png', exif=exifDataBytes)

print(exifData)