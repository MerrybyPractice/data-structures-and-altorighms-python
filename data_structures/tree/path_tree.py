from collections import deque
class Node: 

  def __init__(self, value): 
    self.previous = None
    self.value = value
    self.branches = []

class NonBinaryTree: 

  def __init__(self): 
    self.root = None

  def add_node(self, value): 
    if not self.root: 
      self.root = Node(value)
    else: 
      q = deque()

      for leaf in root.branches: 
        q.appendleft(leaf)

      current = self.root 
      previous = None

      while len(q):

        previous = current 
        current = q.pop() 
        
        for leaf in current.branches: 
          q.appendleft(leaf)

      new_node = Node(value)
      new_node.previous(previous)
      previous.branches(new_node) 

  def contains(self, value): 

    if self.root and value == self.root.value: 

      return self.root


    else: 
      
      q = deque() 

      for leaf in root.branches: 
        q.appendleft(leaf)

      current = self.root

      while len(q): 

        if current.value == value: 
          return current 

        for leaf in current.branches: 
          q.appendleft(leaf) 

        current = q.pop() 

    return False   

  def return_path(self, value1, value2): 
     node2 = self.contains(value2) 

     return_collection = []

     current = node2

     while current: 
       
       return_collection.append(current)
       current = current.previous

     return return_collection.reverse()  




 
            


        


