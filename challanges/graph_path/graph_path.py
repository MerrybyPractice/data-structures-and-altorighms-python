from data_structures.graph.graph import Graph
from data_structures.tree.path_tree import NonBinaryTree

def pathfinder(node1, node2, current): 
  path_tree = NonBinaryTree() 
  path_tree.add_node(current.value)

  if path_tree.contains(node2.value): 
    path_tree.return_path(node1.value, node2.value)
    
