'''

Implementation of a graph using adjacency list.

'''

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbour(self,neighbour,weight=0):
        self.connectedTo[neighbour] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,neighbour):
        return self.connectedTo[neighbour]
    
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

if __name__ == "__main__":
    
    g = Graph()

    for i in range(6):
        g.addVertex(i)

    g.addEdge(0,1,2)

    for vertex in g:
        print(vertex)
        print(vertex.getConnections())
        print()