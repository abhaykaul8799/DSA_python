'''

Create a queue using 2 stacks.

'''

class Queue2Stacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,element):
        if self.stack2 == []:
            self.stack1.append(element)
        else:
            while self.stack2 != []:
                self.stack1.append(self.stack2.pop())
    
    def dequeue(self):
        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()
    
    def size(self):
        return len(self.stack1) + len(self.stack2)

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())