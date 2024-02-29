import os
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return -1  # Return -1 to indicate file not found error

patch = input()
if os.path.exists(patch):
    if os.path.isfile(patch):
        cnt = count_lines(patch)
        print("The .txt file contains", cnt, "lines.")
    else:
        print(f"{patch} is not a .txt file")
else:
    print(f"{patch} does not exist.")