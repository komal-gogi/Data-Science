import os

def rename_files(directory, prefix):
    # Change directory to specified path
    os.chdir(directory)
    # List all the file in the directory
    files = os.listdir()

    # Iterate through each and rename it
    for file in files:
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file):
            # Split the file name and extension
            filename, file_extension = os.path.splitext(file)
            # Construct the new file name with the specified prefix
            new_filename = f"{prefix}_{filename}{file_extension}"
            # Rename the file
            os.rename(file, new_filename)
            # Print a message indicating the file has been renamed
            print(f"Renamed {file} to {new_filename}")


def main():
    # Specify the doirectory containing the files to be renamed
    directory = "C:/Users/yfs3369/OneDrive - Northwestern Mutual/Personal/Python/Testing"
    # Specify the prefix to prepend to each file name
    prefix = "old"
    # Rename files in the specified directory with the specified prefix
    rename_files(directory, prefix)


if __name__ == "__main__":
    main()