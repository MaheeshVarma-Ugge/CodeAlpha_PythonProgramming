import os
import shutil

# Source folder containing jpg files
SOURCE_DIR = r"C:\Users\mahee\pythonproject\CodeAlpha_Python_Programming\Task_Automation_with_Python_Scripts_Task_3\Game_images"

# Destination folder where images will be moved
DEST_DIR = r"C:\Users\mahee\pythonproject\CodeAlpha_Python_Programming\Task_Automation_with_Python_Scripts_Task_3\image"


def move_jpg_files(source, destination):

    # Create destination folder if it doesn't exist
    os.makedirs(destination, exist_ok=True)

    moved = 0

    # Read all files in source folder
    for filename in os.listdir(source):

        # Check for .jpg files
        if filename.lower().endswith(".jpg"):

            # Full source path
            src_path = os.path.join(source, filename)

            # Full destination path
            dest_path = os.path.join(destination, filename)

            # Move file
            shutil.move(src_path, dest_path)

            # Display moved file
            print(f"Moved: {filename} → {destination}")

            moved += 1

    # Final message
    print(f"\nDone! {moved} .jpg file(s) moved.")

    if moved == 0:
        print("No .jpg files found.")


# Run the program
if __name__ == "__main__":

    print(f"Scanning folder: {SOURCE_DIR}\n")

    move_jpg_files(SOURCE_DIR, DEST_DIR)
