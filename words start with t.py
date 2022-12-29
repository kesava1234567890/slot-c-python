s=input("enter the string")
r=s.split()
count=0
for i in r:
    if i.startswith('t') or i.startswith('T'):
      count=count+1
print("the number of words starts in 't' or'T'  ",count)
