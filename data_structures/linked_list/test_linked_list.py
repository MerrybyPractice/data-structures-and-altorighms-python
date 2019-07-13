from .linked_list import LinkedList
from .linked_list import Node

def test_linked_list_exsists(): 
  assert LinkedList()

def test_node_exsists(): 
  assert Node()

def test_linked_list_head_instantiates_as_none(): 
  ll = LinkedList() 
  assert ll.head == None 



"""
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
"""