import os

def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all_directories_files(path):
    print("All Directories and Files:")
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        print("   Files:")
        for file in files:
            print(f"      {file}")
        print()

if __name__ == "__main__":
    path = input("Enter the path: ")

    if os.path.exists(path):
        list_directories_files(path)
        print("\n---------------------------------------------\n")
        list_all_directories_files(path)
    else:
        print("The specified path does not exist.")