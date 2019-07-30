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
        if node.left.value > node.value:
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

      results.append(node.value) 

    visit(self.root) 

    return(results)      

class BinarySearchTree(BinaryTree): 

  def contains(self, value): 

    def visit(node):

      if value == node.value: 
        return True

      if node.left:  
       if visit(node.left) == True: 
         return True


      if node.right: 
        if visit(node.right) == True:
          return True
      return False   
    return visit(self.root)

      

  def add(self, value): 

    def visit(node): 

      if value == node.value: 
        return "Value is already in this list" 

      if value > node.value: 
        if node.right: 
          return visit(node.right)
        else: 
          node.right = Node(value)  
          return f"Node with a value of {value} has been added" 

      if value < node.value: 
        if node.left: 
          return visit(node.left) 
        else: 
          node.left = Node(value) 
          return f"Node with a value of {value} has been added"     

    return visit(self.root)      
