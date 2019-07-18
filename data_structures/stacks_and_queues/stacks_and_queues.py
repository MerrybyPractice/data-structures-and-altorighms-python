from data_structures.linked_list.linked_list import Node
from data_structures.linked_list.linked_list import LinkedList

class Stack: 
  def __init__(self): 
    self.top = None 
    self._list = LinkedList()

  def push(self, value): 
    self._list.insert(value)

    self.top = self._list.head

  def pop(self): 
    if self.top:

      pop_node = self.top

      self.top = self.top.next

      pop_node.next = None

      return pop_node.value

    else: 
      return None  

  def peek(self): 

    if self.top: 

      return self.top.value

    else: 

      return None

class Queue: 

  def __init__(self): 
    self.front = None
    self._list = LinkedList() 

  def enqueue(self, value): 
    if self.front: 
      self._list.append(value) 
      
    else: 
        self._list.insert(value)   
        self.front = self._list.head  

  def dequeue(self): 
    if self.front: 

      dequeue_node = self.front

      self.front = self.front.next 

      dequeue_node.next = None 

      return dequeue_node.value

    else: 

      return None   

  def peek(self): 
    if self.front: 

      return self.front.value 

    else: 

      return None   
