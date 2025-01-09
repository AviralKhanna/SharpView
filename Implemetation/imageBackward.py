import os
from PIL import Image

# Input PPM file path
input_file = r"smoothed_image.ppm"  # Replace with your PPM file path
output_dir = r"implement"     # Output directory for JPEG image

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Ensure the input file has a .ppm extension
if input_file.lower().endswith('.ppm'):
    try:
        # Open the PPM image file
        img = Image.open(input_file)

        # Generate new filename with JPEG extension
        new_filename = os.path.splitext(os.path.basename(input_file))[0] + '.jpg'
        output_path = os.path.join(output_dir, new_filename)

        # Ensure the image is in RGB mode, then save as JPEG
        img = img.convert('RGB')
        img.save(output_path, 'JPEG')

        # Log the successful conversion
        print(f"Successfully converted: {os.path.basename(input_file)} -> {new_filename}")

    except Exception as e:
        # Log the error details if conversion fails
        print(f"Failed to convert {os.path.basename(input_file)}: {str(e)}")
else:
    print("The provided file is not a .ppm file. Please provide a valid PPM file.")

print("Conversion from PPM to JPEG completed!")
