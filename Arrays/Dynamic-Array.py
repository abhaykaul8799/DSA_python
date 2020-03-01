import ctypes

class DynamicArray():
    
    def __init__(self):

        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self,k):

        if not 0<= k < self.n:
            return IndexError("Index is out of bounds!")
        
        return self.A[k]

    def append(self,elem):

        if self.n == self.capacity:
            self._resize(2*self.capacity) # Increase Capacity
        
        self.A[self.n] = elem
        self.n += 1
    
    def _resize(self,new_cap):
        '''
            Resize the existing array to twice its size when it is full
        '''

        B = self.make_array(new_cap)

        for i in range(self.n):
            B[i] = self.A[i]
        
        self.A = B
        self.capacity = new_cap
    
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)() # Grab raw bytes from memory to create array

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[1])
print(arr[0])
print(arr[2]) # To check if error statement works


for i in range(1000):
    arr.append(i)
    print(arr.capacity)