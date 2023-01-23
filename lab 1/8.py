x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

y = "awesome"
def myfunc():
  y = "fantastic"
  print("Python is " + y)
myfunc()
print("Python is " + y)

def myfunc():
  global z
  z = "fantastic"
myfunc()
print("Python is " + z)

w = "awesome"
def myfunc():
  global w
  w = "fantastic"
myfunc()
print("Python is " + w)