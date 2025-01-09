import os
from PIL import Image

# Define the directories for input and output images
input_dir = r"C:\Users\kship\Desktop\Sagar\Frontend\Frontend"  # Input directory should be a folder
output_dir = r"C:\Users\kship\Desktop\Sagar\Frontend\Frontend\enhanced"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.ppm'):
        # Open the PPM image file
        img_path = os.path.join(input_dir, filename)
        try:
            img = Image.open(img_path)

            # Generate new filename with JPEG extension
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            output_path = os.path.join(output_dir, new_filename)

            # Convert to RGB if needed and save the image in JPEG format
            img = img.convert('RGB')  # PPM images should be in RGB, but this ensures conversion
            img.save(output_path, 'JPEG')
            
            
            os.makedirs("Frontend", exist_ok=True)
            with open("Frontend/path.txt", "w") as f:
                f.write(output_path)

            # Output the process information
            print(f"Converted: {filename} -> {new_filename}")
        
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print("Conversion from PPM to JPEG completed!")
