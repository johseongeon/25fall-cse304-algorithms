# name: 
# student id: 
def fib1(n: int) -> int:
    # Complete the code here
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)