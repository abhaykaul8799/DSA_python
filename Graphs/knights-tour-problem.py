'''

Solution of the knight's tour problem using DFS in python.
Given a position on a chessboard, give the sequence of positions
that a knight has to travel so that he visits all the positions
on the chessboard only once.

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

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return (row*bdSize) + col

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i,j in moveOffsets:
        newX = x + i
        newY = y + j
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(cord,bdSize):
    if cord >= 0 and cord < bdSize:
        return True
    else:
        return False

def knightTour(n,path,u,limit):
    '''
    n: current depth in search tree
    path: a list of vertices visited up to this point
    u: the vertex in the graph which we wish to explore
    limit: number of nodes in the graph
    '''

    u.setColor('gray')
    path.append(u)
    if n<limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1,path,nbrList[i],limit)
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done