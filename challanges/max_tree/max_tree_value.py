from data_structures.tree.tree import BinaryTree 
from data_structures.tree.tree import Node 

def max_tree_value(input_tree): 
 
  if input_tree.root:

    holding_value = input_tree.root.value

    def walk(node): 
      nonlocal holding_value
      
      if node.left: 
        walk(node.left)

      if node.value > holding_value:
        holding_value = node.value 

      if node.right: 
        walk(node.right)

      return holding_value

    return walk(input_tree.root) 
  else: 
    return None