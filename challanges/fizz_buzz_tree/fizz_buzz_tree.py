def Fizz_Buzz_Tree(input_tree): 

  def _find_replace(node): 

    if node.value %3 == 0 and node.value %5 == 0: 
      node.value = "FizzBuzz" 
    elif node.value %3 == 0: 
      node.value = "Fizz" 
    elif node.value %5 == 0: 
      node.value = "Buzz"

    if node.left: 
      _find_replace(node.left) 

    if node.right: 
      _find_replace(node.right) 
      
  return _find_replace(input_tree.root)