x = lambda a : a + 10
print(x(5))


y = lambda a,b : a + b
print(y(4,5))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

"""
def myfunc1(n):
  return lambda a : a * n

mytripler = myfunc1(3)
print("Hello)
print(mytripler(11))
"""


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


bo = True
print(type(bo))