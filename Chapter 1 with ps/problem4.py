# write a python program to print the contents of a directory using the os module
# search online for the function which does that
import os

def print_directory_contents(dir_path='.'):
    """
    Print all files and directories in dir_path.
    """
    try:
        entries = os.listdir(dir_path)
    except FileNotFoundError:
        print(f"Error: The directory {dir_path} does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access {dir_path}.")
        return

    print(f"Contents of directory '{dir_path}':")
    for entry in entries:
        print(entry)

def print_files_only(dir_path='.'):
    """
    Print only files (not subdirectories) in dir_path.
    """
    try:
        entries = os.listdir(dir_path)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        return

    print(f"Files in directory '{dir_path}':")
    for entry in entries:
        full_path = os.path.join(dir_path, entry)
        if os.path.isfile(full_path):
            print(entry)

if __name__ == '__main__':
    path_to_list = input("/New folder): ").strip()
    if not path_to_list:
        path_to_list = '.'

    print_directory_contents(path_to_list)
    print()  # blank line
    print_files_only(path_to_list)
