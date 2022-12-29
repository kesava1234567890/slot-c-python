#list1=int(input("enter the list"))
#list1=[1,2,3,4,5]
list1=[]
n=int(input("enter the number of items"))
for i in range(n):
    num=int(input("enter the number"))
    list1.append(num)
print(list1)
odd_count=0
for num in list1:
    if(n % 2 != 0):
        odd_count+=1
print("odd numbers in list1" ,odd_count)
