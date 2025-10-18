import cv2
import os

def extract_frame_and_delete_mov(input_folder):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".mov"):
            mov_path = os.path.join(input_folder, filename)
            jpg_name = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(input_folder, jpg_name)

            print(f"🎞 Processing: {filename}")

            cap = cv2.VideoCapture(mov_path)

            if not cap.isOpened():
                print(f"❌ Could not open video: {filename}")
                continue

            ret, frame = cap.read()
            if ret and frame is not None:
                try:
                    cv2.imwrite(jpg_path, frame)
                    print(f"✅ Saved JPG: {jpg_name}")

                    # Try deleting the MOV
                    try:
                        os.remove(mov_path)
                        print(f"🗑️ Deleted original MOV: {filename}")
                    except Exception as del_error:
                        print(f"❌ Failed to delete {filename}: {del_error}")

                except Exception as e:
                    print(f"❌ Error saving JPG or deleting MOV: {e}")
            else:
                print(f"⚠️ Could not read frame from: {filename}")

            cap.release()

input_folder = r"E:\Iphone"
extract_frame_and_delete_mov(input_folder)
