import os
import ctypes
import time
import itertools
import sys
import random 

def set_wallpaper(image_path):
    try:
        # Change the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")

def get_images_from_folder(folder_path):
    try:
        # Get all image files from the folder
        images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', "tiff"))]
        if not images:
            raise ValueError("No images found in the specified folder.")
        return images
    except Exception as e:
        print(f"Error retrieving images: {e}")
        sys.exit(1)

def rotate_wallpapers(folder_path, interval):
    images = get_images_from_folder(folder_path)
    random.shuffle(images)
    for image in itertools.cycle(images):
        set_wallpaper(image)
        time.sleep(interval)

if __name__ == "__main__":
    folder_path = "D:\\Coding - Learning and Testing\\Python\\wallpaper-rotation\\images"
    interval = 60  # or any other interval you prefer, in seconds

    rotate_wallpapers(folder_path, interval)
