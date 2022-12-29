a=int(input("enter how many numbers you want in this series"))
first = 0
second = 1
for i in range(a):
    print(first)
    temp = first
    first = second
    second = temp+second
    
