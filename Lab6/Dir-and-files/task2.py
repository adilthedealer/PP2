import os
patch = input("Enter the path: ")
if os.path.exists(patch) == True:
    if os.access(patch, os.R_OK):
        print(f"{patch} is readable")
        if os.access(patch, os.W_OK):
            print(f"{patch} is writable")
        else:
            print(f"{patch} is not writable")
    elif os.access(patch, os.W_OK) and not os.access(patch, os.R_OK):
        print(f"{patch} is writable, but not readable")
    else:
        print(f"{patch} is not readable")
else:
    print(f"{patch} does not exist")
