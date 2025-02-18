import os

def change_file_extension(folder_path):
    for file in os.listdir(folder_path):
        if file.lower().endswith(".mp3"):
            os.rename(folder_path + "/" + file, folder_path + "/" + file.casefold().replace(".Mp3", ".mp3"))

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    change_file_extension(folder_path)