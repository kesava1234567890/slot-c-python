a=int(input("enter the first mark"))
b=int(input("enter the second mark"))
c=int(input("enter the third mark"))
d=a+b+c
e=d/3
if(e>=90):
   print("a:grade")
elif(e>=80):
   print("b:grade")
elif(e>=70):
   print("c:grade")
elif(e>=50):
   print("d:grade")
else:
   print("fail")
