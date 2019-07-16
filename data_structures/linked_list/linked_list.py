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

    while current.next != None: 
      
      current = current.next  

    insert = Node(value) 

    current.next = insert  

  def insert_before(self, value, new_val): 

    current = self.head 

    try: 
      if current.value != value: 
        while current.next.value != value: 
        
          current = current.next     

        insert = Node(new_val, current.next) 
        current.next = insert
      else: 
        insert = Node(new_val, current)  

        self.head = insert
      

    except AttributeError: 
      print(value, " not found in this Linked List")      

  def insert_after(self, value, new_val): 
    
    current = self.head 
    
    while current.value != value: 
      current = current.next 
      
    if current.value == value: 
      
      current.next = Node(new_val, current.next) 

  def kth_from_the_end(self, k): 
    
    current = self.head 
    total = 0

    while current: 
      current = current.next 
      total += 1
    
    if k > total: 
      return

    idx = total - k - 1 

    current = self.head

    for i in range(idx): 

      current = current.next
    if current:   
      return current.value  
    else: 
      return   

    
      

class Node: 

  def __init__(self, value, next = None): 
    self.value = value
    self.next = next
