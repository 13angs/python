import os

def rename_images_in_directory(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file contains a space in its name
        containing = ' '
        if containing in filename:
            # Create the new filename by replacing spaces with hyphens
            new_filename = filename.replace(containing, '-')
            # Get the full path for the old and new filenames
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Define the directory containing the images
data_directory = 'data'

# Run the function to rename the images
rename_images_in_directory(data_directory)
