N = int(input())

def fib(N):
    if N <= 1:
        return 1
    else:
        return fib(N-1) + fib(n-2)

print(fib(3))