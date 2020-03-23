'''

Implementation of queue in python.

'''

class Queue:

    def __init__(self):
        self.q = []
    
    def enqueue(self,x):
        self.q.insert(0,x)
    
    def isEmpty(self):
        return self.q == []
    
    def dequeue(self):
        return self.q.pop()
    
    def size(self):
        return len(self.q)

q = Queue()
q.enqueue("Abhay")
q.enqueue("Kaul")
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())

