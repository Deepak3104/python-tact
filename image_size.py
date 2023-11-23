import cv2 
from PIL import Image
from datetime import date
import piexif
import os
from PIL.ExifTags import TAGS
import rasterio

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

def inject_exif(
    filepath, destination_folder_path, 
    folder_name, 
    model_height, model_weight, 
    model_measurements
):
    today = date.today()
    dict =  {
        'admin_pick'            : 1,
        'igh'                   : folder_name,
        'model_height'          : model_height,
        'model_weight'          : model_weight,
        'model_measurements'    : model_measurements,
        'updated_date'          : today, # should be current dates
    }

    pass
def inject_exif_on_folder(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # Open the image using Pillow
                img = Image.open(file_path)

                # Add or update Exif data
                img_exif = img.info.get('exif', {})
                img_exif.update(exifData)
                img.info['exif'] = img_exif

                # Save the modified image
                img.save(file_path)

                print(f"Exif data injected successfully into: {file_path}")

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

folder_path = '/home/deepak/Downloads'

inject_exif_on_folder(folder_path)