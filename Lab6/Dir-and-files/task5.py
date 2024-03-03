mylist = ["Open\n", "Close\n", "Flush\n", "Delete\n"]
s = ''.join(mylist)
file = open("actions.txt", "w")
file.write(s)