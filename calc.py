a=int(input('select 1 for addition /n 2 for subtraction /n 3 for multiplication /n 4 for division /n 5 for exponent /n 6 for sin and 7 for cos'))
if a==1:
    b=int(input("enter first number"))
    c=int(input('enter second number'))
    print(b+c)
if a==2:
    b=int(input("enter first number"))
    c=int(input('enter second number'))
    if b>c:
        print(b-c)
    else:
        print(c-b)
if a==3:
    b=int(input("enter first number"))
    c=int(input('enter second number'))
    print(c*b)
if a==4:
    b=int(input("enter first number"))
    c=int(input('enter second number'))
    if c==0:
        print('div by zero not possible')
    else:
        print(b/c)
if a==5:
    b=int(input("enter base "))
    c=int(input('enter power '))
    print(b**c)
import math
def sin(x): 
     d = 0 
     for i in range(0,60): 
         if i%2 == 0: 
             n = (2 * i) + 1 
             d += (x ** n)/math.factorial(n) 
         else: 
             n = (2 * i) + 1 
             d -= (x ** n) /math.factorial(n) 
     return d
if a==6:
     b=float(input('enter angel in radian'))
     print(sin(b))
if a==7:
    b=float(input('enter the angel in radian'))
    c=sin(b)
    f=1-(c**2)
    g=f**(1/2)
    if b>math.pi/2:
        print(-g)
    else:
        print(g)
    

    
