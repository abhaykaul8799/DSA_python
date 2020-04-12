'''

Given a string, find all the permutations of the string using recursion.

'''

def permutation(s):
    
    out = []

    if len(s) <=1 :
        out =  [s]
    
    else:
        for i,letter in enumerate(s):
            for perm in permutation(s[:i]+s[i+1:]):
                out += [letter+perm]
    return out

print(permutation("1234"))