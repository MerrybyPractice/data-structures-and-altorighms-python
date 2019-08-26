from collections import deque

class Graph: 

  def __init__(self): 
    self._vertices = [] 

  def add_vertex(self, value): 
    vrtx = Vertex(value)
    self._vertices.append(vrtx) 
    return vrtx

  def add_edge(self, vrtx1, vrtx2, weight=0):
    if vrtx1 in self._vertices and vrtx2 in self._vertices:
      vrtx1.neghibors.append(Edge(vrtx2, weight))   

  def get_vertices(self): 
    return self._vertices or None   

  def get_neghibors(self, vertex): 
    return vertex.neghibors

  def breadth_first(self, root, operation):   
    q = deque()

    q.appendleft(root) 

    to_reset = set()

    while q: 
      current = q.pop()
      current.visited = True
      to_reset.add(current)

      operation(current)

      for edge in current.neghibors: 
        if not edge.vertex.seen: 
          q.appendleft(edge.vertex)

    for vertex in to_reset: 
      vertex.visited = False

  def __len__(self): 
    return len(self._vertices)  

class Edge: 
  def __init__(self, vertex, weight=0): 
    self.vertex = vertex
    self.weight = weight

class Vertex: 
  def __init__(self, value): 
    self.value = value
    self.neghibors = []
    self.seen = False