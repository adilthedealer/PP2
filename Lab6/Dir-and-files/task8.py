import os
p = input("Enter the path: ")
if os.path.exists(p):
    if os.path.isfile(p):
        if os.access(p, os.W_OK) and os.access(p, os.R_OK):
            os.remove(p)
        else:
            print("Not accessible")
    else:
        print("Path is a directory")
else:
    print("Path does not exist")