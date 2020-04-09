'''

Calculate cumulative sum of a whole number till 0 using recursion.

'''

def rec_sum(n):
    
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

for i in range(10):
    print(rec_sum(i))