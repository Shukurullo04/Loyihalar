import random
def f():
 x=random.randint(1,50)
 y=random.randint(1,50)
 z=int(input(str(x)+" + "+str(y)+" = "))
 if z==x+y :
  print("To'g'ri")
  f()
 else:
  print("Notug'ri")
  f()
f()
