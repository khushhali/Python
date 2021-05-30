'''
Program to chech roots of a quadeq

format of quad eq -> ax^2 + bx + c
'''
a = float(input('enter cofficient of x square (a):- '))
b = float(input('enter cofficient of x (b) :- '))
c = float(input('enter constant (c) :- '))

roots1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
roots2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(roots1)
print(roots2)
