def fibanocci(i):
    if i==0:
       return 0
    elif i== 1:
       return 1
    else:
        return fibanocci(i-2) + fibanocci(i-1)

for x in range(13):
    print(fibonacci(x))
    
