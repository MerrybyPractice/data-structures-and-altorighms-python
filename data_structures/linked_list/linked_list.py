"""
Streatch Goal doubbly linked***     
"""
class LinkedList: 

  def __init__(self): 
    self.head = None

  def insert(self, value):
    self.head = Node(value, next = self.head) 

  def includes(self, value): 
      current = self.head

      while current != None: 
          print(current.value, value)

          if current.value == value: 
            return True
          current = current.next 
      return False    

  def __str__(self): 
    current = self.head 

    return_string = ""

    while current != None: 
      return_string += str(current.value)
      if current.next: 
        return_string += " > "
      current = current.next 

    return return_string  

class Node: 
  
  def __init__(self, value, next = None): 
    self.value = value
    self.next = next
