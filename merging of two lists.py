b=int(input("enter a number"))
for i in range(2,b,1):
    if(b%i == 0):
        print("the num is not a prime number")
        break
    else:
        print("the num is a prime number")
    
    
