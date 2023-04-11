import os

def replace_spaces_with_underscores(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for file_name in files:
        # Check if the file name contains spaces
        if ' ' in file_name:
            # Replace spaces with underscores
            new_file_name = file_name.replace(' ', '_')

            # Rename the file
            old_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_file_name)
            os.rename(old_path, new_path)
            print(f'Renamed: "{file_name}" -> "{new_file_name}"')

if __name__ == "__main__":
    # Specify the directory where you want to update file names
    
    target_directory = "../content/Civil_Engineering"

    # Call the function to update file names
    replace_spaces_with_underscores(target_directory)