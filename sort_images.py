import os
import shutil

# Path to the main Leaves folder
leaves_folder = "leaf_dataset/Leaves"
# Path to the folder containing images to add (change this path as needed)
source_folder = os.path.join(leaves_folder, "ToAdd")  # Place new images here

# Dynamically get class names: all non-empty folders in leaves_folder, excluding special folders
exclude_folders = {"ToAdd", "Unknown", "Unsorted"}
class_names = []
for folder in os.listdir(leaves_folder):
    folder_path = os.path.join(leaves_folder, folder)
    if (
        os.path.isdir(folder_path)
        and folder not in exclude_folders
        and any(os.scandir(folder_path))  # Only include non-empty folders
    ):
        class_names.append(folder)

# Create class folders if they don't exist (for future-proofing, not strictly needed)
for class_name in class_names:
    class_folder = os.path.join(leaves_folder, class_name)
    os.makedirs(class_folder, exist_ok=True)

# Copy all images from source_folder to a class folder if prefix matches, otherwise copy to 'Unsorted'
unsorted_folder = os.path.join(leaves_folder, 'Unsorted')
os.makedirs(unsorted_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    moved = False
    for class_name in class_names:
        if filename.lower().startswith(class_name.lower()):
            src = os.path.join(source_folder, filename)
            dst = os.path.join(leaves_folder, class_name, filename)
            shutil.copy2(src, dst)
            print(f"Copied {filename} to {class_name}/")
            moved = True
            break
    if not moved:
        # Copy to Unsorted if no class matches
        src = os.path.join(source_folder, filename)
        dst = os.path.join(unsorted_folder, filename)
        shutil.copy2(src, dst)
        print(f"Copied {filename} to Unsorted/")

print("Image sorting complete. Check your class folders!")
