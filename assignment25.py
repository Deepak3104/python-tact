import os
from PIL import Image
from PIL.ExifTags import TAGS
import warnings
import rasterio
warnings.filterwarnings("ignore", category=rasterio.errors.NotGeoreferencedWarning)

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def update_exif_with_dimensions(image_path):
    # Get existing Exif data
    img = Image.open(image_path)
    exif_data = img.info.get('exif', {})

    # Get image dimensions
    width, height = get_image_dimensions(image_path)

    # Update Exif data with dimensions
    exif_data.update({
        "Width": width,
        "Height": height,
        "file_path": image_path,
        "destination_folder_path": folder_path,

    })

    # Save the modified image
    img.save(image_path)

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

# Example usage:
folder_path = '/home/deepak/Downloads'
process_images_in_folder(folder_path)
