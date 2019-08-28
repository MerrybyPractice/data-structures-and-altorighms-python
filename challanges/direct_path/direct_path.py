from data_structures.graph.graph import Graph

def direct_path(g, lst): 
  
  total_edge_weight = 0
  current_node = None
  previous_node = None

  while lst: 
    for vert in g.vertices: 
      if lst[0] == vert.value: 
        current_node = vert
        previous_node = lst.pop(0)

    for item in lst: 
        if item in current_node.neghibors.value: 
          total_edge_weight = total_edge_weight + current_node.neghibors.weight 
        else: 
          return [False, 0]  
  return [True, total_edge_weight]        