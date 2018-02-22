'''

fib(n) = 1 if n=1,2
         fib(n-1) + fib(n-2) otherwise

'''

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

limit = int(input("Enter the limit upto n terms>>>"))
list = [fib(x) for x in range(1,limit+1)]
print(list)