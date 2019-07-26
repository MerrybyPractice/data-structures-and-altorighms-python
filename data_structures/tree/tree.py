class Node: 

  def __init__(self, value): 
    self.value = value 
    self.left = None 
    self.right = None 

class BinaryTree: 

  def __init__(self):     
    self.root = None

  def in_order_traversal(self): 

    results = []

    def visit(node):

      if node.left: 
        visit(node.left)

      results.append(node.value)

      if node.right: 
        visit(node.right)

    visit(self.root)    

    return results 

  def pre_order_traversal(self): 

    results = [] 

    def visit(node): 

      results.append(node.value) 

      if node.left: 
        visit(node.left) 

      if node.right: 
        visit(node.right) 

    visit(self.root) 

    return results    

  def post_order_traversal(self):     

    results = []

    def visit(node): 

      if node.left: 
        visit(node.left) 

      if node.right: 
        visit(node.right) 

      results.appent(node.value) 

    visit(self.root) 

    return(results)      
