'''

Implementation of stack in python.

'''

class Stack:

    def __init__(self):
        self.items = []
    
    def push(self,x):
        self.items.append(x)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) < 1
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push("Abhay")
s.push("Kaul")
s.push("20")
print(s.size())
print(s.peek())
print(s.pop())
print(s.peek())