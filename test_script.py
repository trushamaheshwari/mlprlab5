import os
import glob

# Check if Jupyter Notebook files exist
notebooks = glob.glob("*.ipynb")
if notebooks:
    print(f"✅ Found Jupyter Notebook files: {notebooks}")
else:
    print("❌ No Jupyter Notebook files found!")

# Check if images exist in the images folder
image_extensions = ["*.png", "*.jpg", "*.jpeg", "*.gif"]
image_files = []
for ext in image_extensions:
    image_files.extend(glob.glob(f"images/{ext}"))

if image_files:
    print(f"✅ Found image files: {image_files}")
else:
    print("❌ No image files found in the images/ folder!")

# Check if dataset files exist
dataset_files = glob.glob("data/*")
if dataset_files:
    print(f"✅ Found dataset files: {dataset_files}")
else:
    print("❌ No dataset files found in the data/ folder!")

# Exit with failure if any check fails
if not notebooks or not image_files or not dataset_files:
    exit(1)



