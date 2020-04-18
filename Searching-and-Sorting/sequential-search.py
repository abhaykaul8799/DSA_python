'''

Implementation of sequential search.

'''

from random import randint

l = []
for i in range(500):
    l.append(randint(1,999))

x = randint(1,999)

flag = False
print("Number to be searched for: ",x)
for i in l:
    if x == i:
        flag = True
        break
if flag:
    print("Element found")
else:
    print("Element not found.")
