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