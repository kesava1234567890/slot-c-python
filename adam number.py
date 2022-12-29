number=int(input())
reverse=int(str(number)[::-1])
number_sqr=int(number)**2
reverse_sqr=reverse**2

if number_sqr==int(str(reverse_sqr)[::-1]):
    print("adam number")
else :
    print("not an adam number")
