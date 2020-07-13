'''

Alternate implementation of BFS.

'''


graph = { 'A' : set(['B','C']),
          'B' : set(['A','D','E']),
          'C' : set(['A','F']),
          'D' : set(['B']),
          'E' : set(['B','F']),
          'F' : set(['C','E'])
        }

def bfs(graph,start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph,start,goal):
    queue = [(start,[start])]
    while queue:
        (vertex,path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next,path+[next]))

print(bfs(graph,'A'))
print(list(bfs_paths(graph,'A','F')))