class FClass:
    def __init__(self, printString):
        self.string = printString.upper()

    def pr(self):
        print(self.string)
printString = input()
ffs = FClass(printString)
ffs.pr()
