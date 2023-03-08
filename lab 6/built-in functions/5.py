my_tuple = (True, True, False, True)

if all(my_tuple): #all() - returns True if all items in an iterable object are true
    print("All elements of the tuple are true")
else:
    print("At least one element of the tuple is false")