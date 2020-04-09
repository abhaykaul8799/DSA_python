'''

Calculate the sum of the digits using recursion.

'''

def dig_sum(num):
    if num==0:
        return 0
    else:
        return num%10 + dig_sum(num//10)

def checker(num):
    return sum(list(map(int,[i for i in str(num)])))

flag = True
for i in [1234,2131,123456,918241924,13812319,128312,999999999]:
    ans = dig_sum(i)
    check = checker(i)
    if ans != check:
        flag = False
        print("Wrong Code, Try Again.")

if flag:
    print("All test cases passed.")