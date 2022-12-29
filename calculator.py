#1.add
#2.subtract
#3.multiply
#4.divide
print("select an operation to perform")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

operation=input()

if operation =="1":
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    print("the sum is " + str(int(num1)+int(num2)))
elif operation =="2":
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    print("the difference is " + str(int(num1)-int(num2)))
          
elif operation =="3":
   num1=int(input("enter the first number"))
   num2=int(input("enter the second number"))
   print("the product is "+ str(int(num1)*int(num2)))
         
elif operation =="4":
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    print("the division of "+ str(int(num1)/ int(num2)))
else:
      print("invalid entry")
  
