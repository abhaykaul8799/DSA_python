'''

Breadth First Search implementation on graphs using python.

'''

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None
    
    def addNeighbour(self,neighbour,weight=0):
        self.connectedTo[neighbour] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,neighbour):
        return self.connectedTo[neighbour]
    
    def setColor(self,clr):
        self.color = clr
    
    def getColor(self):
        return self.color
    
    def setDistance(self,dstnce):
        self.distance = dstnce
    
    def getDistance(self):
        return self.distance
    
    def setPred(self,vertx):
        self.pred = vertx
    
    def getPred(self):
        return self.pred
    
    def __str__(self):
        
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])
    
class Graph:

    def __init__(self):
        self.vertList = {} # Adjacency List
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def addEdge(self,frm,to,cost=0):
        if frm not in self.vertList:
            nv = self.addVertex(frm)
        if to not in self.vertList:
            nv = self.addVertex(to)
        self.vertList[frm].addNeighbour(self.vertList[to],cost)
    
    def getVerticies(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self,n):
        return n in self.vertList

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


def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()) > 0:
        currentVert = vertQueue.dequeue()
        for neighbour in currentVert.getConnections():
            if (neighbour.getColor() == 'white'):
                neighbour.setColor('grey')
                neighbour.setDistance(currentVert.getDistance()+1)
                neighbour.setPred(currentVert)
                vertQueue.enqueue(neighbout)
        currentVert.setColor('black')
