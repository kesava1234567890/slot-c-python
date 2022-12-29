#ax**2+bx+c
a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))
d=b**2-4*a*c
if (d>0):
    print("the roots are real")
elif(d==0):
    print("the roots are real and equal")
elif(d<0):
    print("the roots are non real")
else:
    print("the roots are real and unequal")
    
