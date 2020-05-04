'''

Alternate Implementation of graphs in python

'''

from enum import Enum

class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

from collections import OrderedDict

class Node:

    def __init__(self,num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict() 
    
    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()
    
    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node
    
    def add_edge(self,src,dest,weight=0):
        if src not in self.nodes:
            self.add_node(src)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[src].adjacent[self.nodes[dest]] = weight # Sources adjacency list, which holds weight as value and adjacent nodes as key

g = Graph()

g.add_edge(0,1,5)
g.add_edge(1,2,2)
g.add_edge(0,3,1)
print()
print("Nodes in the graph with their keys")
print(g.nodes)
print()
print("Nodes adjacent to first node")
print(g.nodes[0].adjacent)
print()
print("Weight of edge from node 0 to node 1")
print(g.nodes[0].adjacent[g.nodes[1]])
