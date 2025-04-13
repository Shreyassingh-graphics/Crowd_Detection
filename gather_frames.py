import os
import shutil

source_root = "frames"
output_folder = "all_frames"
os.makedirs(output_folder, exist_ok=True)

for scene_folder in os.listdir(source_root):
    scene_path = os.path.join(source_root, scene_folder)
    if os.path.isdir(scene_path):
        for filename in os.listdir(scene_path):
            if filename.endswith(".jpg"):
                full_path = os.path.join(scene_path, filename)
                new_path = os.path.join(output_folder, f"{scene_folder}_{filename}")
                shutil.copy(full_path, new_path)

print("All frames gathered into:", output_folder)
