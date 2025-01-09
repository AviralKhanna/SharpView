# from PIL import Image

# def convert_to_ppm(input_file, output_file):
#     # Open the image using Pillow
#     with Image.open(input_file) as img:
#         # Convert and save to PPM format
#         img.save(output_file, format='PPM')
#         print(f"Converted {input_file} to {output_file}")

# if __name__ == "__main__":
#     # Replace 'input.jpg' and 'output.ppm' with your desired file names
#     input_file = r"V:\Minor Project 1\Code\VK1.jpg"  # or input.png
#     output_file = "VK.ppm"
    
#     convert_to_ppm(input_file, output_file)
from PIL import Image

def convert_to_ppm(input_file, output_file, target_resolution=(1920, 1080)):
    """
    Convert the image to PPM format after resizing it to the target resolution.

    Parameters:
    input_file (str): Path to the input image file.
    output_file (str): Path to the output PPM file.
    target_resolution (tuple): Target resolution for the image (width, height).
    """
    # Open the image using Pillow
    with Image.open(input_file) as img:
        # Print the original resolution
        print(f"Original resolution: {img.size}")

        # Check if the image is larger than the target resolution
        if img.size[0] > target_resolution[0] or img.size[1] > target_resolution[1]:
            # Resize the image while maintaining the aspect ratio
            img.thumbnail(target_resolution, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsampling
            print(f"Resized to: {img.size}")

        # Convert and save to PPM format
        img.save(output_file, format='PPM')
        print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    # Specify input and output file paths
    input_file = r"WhatsApp Image 2024-10-07 at 11.46.10.jpeg"  # Input image file path (JPEG/PNG)
    output_file = "image.ppm"  # Output PPM file path

    # Define the target resolution for resizing (e.g., 1920x1080)
    target_resolution = (1920, 1080)  # Full HD resolution for faster processing
    
    # Convert to PPM after resizing
    convert_to_ppm(input_file, output_file, target_resolution)
