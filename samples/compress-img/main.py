import os
from PIL import Image

# Function to compress images
def compress_image(input_path, output_path, quality=85):
    """
    Compresses the image at input_path and saves it to output_path with the specified quality.
    
    Parameters:
    input_path (str): The path to the input image file.
    output_path (str): The path where the compressed image will be saved.
    quality (int): The quality of the output image (1-100). Higher means better quality.
    """
    # Open the image file
    with Image.open(input_path) as img:
        # Save the image with the specified quality
        img.save(output_path, optimize=True, quality=quality)

# Directory containing the images to compress
input_directory = 'data/'
# Directory to save the compressed images
output_directory = 'compressed_data/'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_directory):
    # Check if the file is an image (you can add more formats if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Construct the full input path
        input_path = os.path.join(input_directory, filename)
        # Construct the full output path
        output_path = os.path.join(output_directory, filename)
        
        # Compress the image
        compress_image(input_path, output_path, 70)
        print(f'Compressed and saved: {output_path}')

print("Image compression completed.")