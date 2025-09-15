import math

def findRoots(a,b,c):
    d = b*b - 4*a*c

    if d>= 0:
        x1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
        x2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
        return(x1,x2)
    else:
        return("complex roots")

a = float(input("input a: "))
b = float(input("input b: "))
c = float(input("input c: "))
print(findRoots(a,b,c))