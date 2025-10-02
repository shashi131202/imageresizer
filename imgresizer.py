import os
from PIL import Image
import shutil

def resize_images(input_folder, output_folder, width=800, height=600, output_format="JPEG"):
    # If output folder exists, clear it so resized images are always updated
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        try:
            with Image.open(file_path) as img:
                # Resize image
                resized_img = img.resize((width, height))

                # Extract file name without extension
                base_name = os.path.splitext(filename)[0]

                # Save in desired format (default: JPEG)
                save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                resized_img.save(save_path, output_format)

                print(f"✅ Resized and saved: {save_path}")
        except Exception as e:
            print(f"❌ Could not process {filename}: {e}")

if __name__ == "__main__":
    input_folder = "images"     # folder with original images
    output_folder = "output"    # resized images saved here

    # Change these values anytime, output will always be regenerated
    resize_images(input_folder, output_folder, width=400, height=800, output_format="PNG")
