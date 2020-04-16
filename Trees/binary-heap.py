'''

Implementation of Binary Heap using a list
in python ( A single list can be used to 
represent a complete binary tree).

'''

# Min key Heap
class BinaryHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percolateUp(self,i):
        while i//2>0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percolateUp(self.currentSize)
    
    def minChild(self,i):
        if i*2 + 1> self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1
    
    def percolateDown(self,i):

        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
    
    def delMin(self):
        returnVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percolateDown(1)
        return returnVal
    
    def buildHeap(self,a_list):
        i = len(a_list) // 2 # Because after the halfway point, all nodes are leaves
        self.currentSize = len(a_list)
        self.heapList = [0] + a_list[:]
        while (i > 0):
            self.percolateDown(i)
            i -= 1
    
    

    
    
