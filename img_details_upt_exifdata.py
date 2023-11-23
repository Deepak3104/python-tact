import os
from dotenv import load_dotenv
import rasterio
from PIL import Image
from PIL.ExifTags import TAGS
import warnings
warnings.filterwarnings("ignore", category=rasterio.errors.NotGeoreferencedWarning)

# Load environment variables from .env file
load_dotenv()

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def update_exif_with_dimensions(image_path):
    # Open the image using rasterio
    with rasterio.open(image_path, 'r') as src:
        # Get existing Exif data
        exif_data = src.tags()

        # Get image dimensions
        width, height = get_image_dimensions(image_path)

        # Update Exif data with dimensions
        exif_data.update({
        "Width": width,
        "Height": height,
        "file_path": image_path,
        "destination_folder_path": folder_path,

    })
    # Write the updated Exif data back to the image
    with rasterio.open(image_path, 'r+') as src:
        src.update_tags(**exif_data)

    return exif_data

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is a PNG or JPEG image
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Update Exif data with dimensions and get the updated data
                updated_exif_data = update_exif_with_dimensions(file_path)

                # Display Exif data in dictionary format
                print(f"\nExif Data for {filename}:")
                for tag, value in updated_exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    print(f"{tag_name}: {value}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Get folder path from the environment variable
folder_path = os.getenv("FOLDER_PATH")

if folder_path:
    process_images_in_folder(folder_path)
else:
    print("Error: FOLDER_PATH not specified in the .env file.")
