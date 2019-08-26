class Graph: 

  def __init__(self): 
    self._vertices = [] 

  def add_vertex(self, value): 
    vrtx = Vertex(value)
    self._vertices.append(vrtx) 
    return vrtx

  def get_vertices(self): 
    return self._vertices or None   

  def __len__(self): 
    return len(self._vertices)  

class Vertex: 
  def __init__(self, value): 
    self.value = value