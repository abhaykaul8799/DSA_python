'''

Implement the fibonacci sequence in three ways:
1. Recursively
2. Memoization (DP)
3. Iteratively

'''

def rec_fibo(n):

    if 0<=n<=1:
        return n
    
    else:
        return rec_fibo(n-1) + rec_fibo(n-2)

temp = [None] * 1000

def mem_fibo(n):

    if n==1:
        return 1
    if n==0:
        return 0
    
    if not temp[n]:
        temp[n] = mem_fibo(n-1) + mem_fibo(n-2)
    
    return temp[n]

def iter_fibo(n):
    a,b = 0,1
    for i in range(n):
        a,b= b,a+b
    return a



print(rec_fibo(10))

print(mem_fibo(10))

print(iter_fibo(10))