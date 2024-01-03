import os
import shutil

def organize_files(source_folder):
    # Define categories and their corresponding file extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Others': []  # Files with unknown or no extension
    }

    # Create folders for each category if they don't exist
    for category in categories:
        folder_path = os.path.join(source_folder, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            # Get the file extension (including the dot)
            _, file_extension = os.path.splitext(filename)

            # Determine the category for the file
            assigned_category = 'Others'  # Default category
            for category, extensions in categories.items():
                if file_extension.lower() in extensions:
                    assigned_category = category
#                     break
#
#             # Move the file to the respective category folder
#             destination_folder = os.path.join(source_folder, assigned_category)
#             shutil.move(file_path, os.path.join(destination_folder, filename))
#             print(f'Moved {filename} to {assigned_category} folder.')
#
# if __name__ == '__main__':
#     source_directory = input('Enter the path of the directory to organize: ')
#     organize_files(source_directory)
