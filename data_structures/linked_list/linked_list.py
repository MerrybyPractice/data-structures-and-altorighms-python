"""
Streatch Goal doubbly linked***   
  .append(value) which adds a new node with the given value to the end of the list
  .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
  .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
"""
class LinkedList: 

  def __init__(self): 
    self.head = None

  def insert(self, value):
    self.head = Node(value, next = self.head) 

  def includes(self, value): 
      current = self.head

      while current != None: 

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

  def append(self, value): 
    current = self.head 

    while current != None: 
      current = current.next
      if current.next == None: 
        insert = Node(value) 
        current.next = insert
        
  def insert_before(self, value, new_val): 
    current = self.head 

    while current != value: 
      current = current.next 
      if current.next.value == value:
        insert = Node(value) 
        holding = current.next
        current.next = insert 
        insert.next = holding


class Node: 

  def __init__(self, value, next = None): 
    self.value = value
    self.next = next
