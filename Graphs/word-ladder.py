'''

Word ladder example code.
Move from one word to another while only changing
one letter at a time.

'''

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self,neighbour,cost=0):
        self.connectedTo[neighbour] = cost
    
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
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        newVertex = Vertex(key)
        self.numVertices += 1
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    def addEdge(self,frm,to,cost=0):
        if frm not in self.vertList:
            nv = self.addVertex(frm)
        if to not in self.vertList:
            nv = self.addVertex(to)
        self.vertList[frm].addNeighbour(self.vertList[to],cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self,n):
        return n in self.vertList
    
def buildGraph(wordFile):
    d = {}
    g = Graph()

    wfile = open(wordFile,'r')

    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

g = buildGraph("words-4-word-ladder.txt")
for i in g: print(i)
    
