import os
import hashlib
from PIL import Image
import pillow_heif

def image_hash(image_path):
    with Image.open(image_path) as img:
        img = img.resize((256, 256)).convert('RGB')
        return hashlib.md5(img.tobytes()).hexdigest()

def convert_heic_to_jpg_delete_original(input_path):
    try:
        heif_file = pillow_heif.read_heif(input_path)
        image = Image.frombytes(
            heif_file.mode, heif_file.size, heif_file.data
        )

        output_path = os.path.splitext(input_path)[0] + ".jpg"
        image.save(output_path, format="JPEG")
        os.remove(input_path)
        print(f"✔ Converted and deleted: {input_path}")
        return output_path
    except Exception as e:
        print(f"❌ Failed for {input_path}: {e}")
        return None

def remove_duplicate_jpgs(folder_path):
    seen_hashes = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg"):
            full_path = os.path.join(folder_path, filename)
            try:
                h = image_hash(full_path)
                if h in seen_hashes:
                    os.remove(full_path)
                    print(f"🗑️ Duplicate deleted: {filename}")
                else:
                    seen_hashes[h] = full_path
            except Exception as e:
                print(f"❌ Error hashing {filename}: {e}")

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            full_path = os.path.join(folder_path, filename)
            convert_heic_to_jpg_delete_original(full_path)
    
    remove_duplicate_jpgs(folder_path)

# 🔁 Set your folder path here
process_folder("E:\Family\Arooj")  # ← change to your folder path
