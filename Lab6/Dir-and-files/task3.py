import os
patch = input("Enter the path: ")
if os.path.exists(patch):
    if os.path.isfile(patch):
        print("Directory:", os.path.dirname(patch))
        print("Filename:", os.path.basename(patch))
    elif os.path.isdir(patch):
        print(f"{patch} is a directory")
        print(os.path.basename(patch))
else:
    print(f"{patch} does not exist")