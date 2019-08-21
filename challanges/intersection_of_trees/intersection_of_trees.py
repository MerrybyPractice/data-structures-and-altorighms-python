from data_structures.tree.tree import BinaryTree

def intersection_traversal(node): 

  tree_dict = {}

  if node.value not in tree_dict: 
    tree_dict.add(node.value, 1)

  else: 
    tree_dict[node.value] = tree_dict[node.value] + 1  

  if node.left: 
    intersection_traversal(node.left)

  if node.right: 
    intersection_traversal(node.right)  

  return tree_dict  

def tree_intersection(tree_1, tree_2): 
  tree_dict = intersection_traversal(tree_1.root)
  tree_dict + intersection_traversal(tree_2.root)

  return_lst = [] 
  for item in tree_dict: 
    if item.value >=2: 
      return_lst.append(item.key)

  return return_lst    

  
