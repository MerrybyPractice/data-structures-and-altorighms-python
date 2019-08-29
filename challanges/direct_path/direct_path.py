from data_structures.graph.graph import Graph

def direct_path(g, lst): 
  
  total_edge_weight = 0
  current_node = None
  previous_node = None

  while lst: 
    for vert in g._vertices: 
      if lst: 
        if lst[0] == vert.value: 
          current_node = vert
          previous_node = lst.pop(0)

    found = False
    for item in lst: 
      #vertex_lst = []
      for edge in current_node.neghibors:
        if item == edge.vertex.value: 
          total_edge_weight = total_edge_weight + edge.weight 
          found = True
          break

    if not found:
      return [False, 0] 

  if found: 
    return [True, total_edge_weight]
      
   
          