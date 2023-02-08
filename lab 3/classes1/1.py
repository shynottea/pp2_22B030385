class myClass:
    def getString(self):
        n = str(input("Input a string: "))
        return n
    def printString(self, string):
        print(string.upper())

a = myClass()
string = a.getString()
a.printString(string)