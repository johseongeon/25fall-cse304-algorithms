# name: 
# student id: 
def fib2(n: int) -> int:
    f = [0] * (n + 1)
    # Complete the code here

    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    f[0], f[1] = 0, 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    
    return f[n]