def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
num=int(input("Enter the Number :"))
print(fib(num+1))
