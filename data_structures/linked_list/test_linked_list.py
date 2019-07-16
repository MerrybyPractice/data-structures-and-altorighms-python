from .linked_list import LinkedList
from .linked_list import Node

def test_linked_list_exsists(): 

  assert LinkedList()

def test_node_exsists(): 

  assert Node(0)

def test_linked_list_head_instantiates_as_none(): 
  ll = LinkedList() 

  assert ll.head == None 

def test_node_insert(): 
  ll = LinkedList()
  ll.insert(1)

  assert ll.head.value == 1
  assert ll.head.next == None

def test_node_insert_seccond_node(): 
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)

  assert ll.head.value == 2
  assert ll.head.next.value == 1
  assert ll.head.next.next == None


def test_node_insert_many_node(): 
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)

  assert ll.head.value == 3
  assert ll.head.next.value == 2
  assert ll.head.next.next.value == 1
  assert ll.head.next.next.next == None

def test_includes(): 
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)

  assert ll.includes(1) is True



def test_does_not_include(): 
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)

  assert ll.includes(357) is False

def test_includes_at_head(): 
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)

  assert ll.includes(3) is True

def test_to_string(): 
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(3)

  stringify = str(ll)

  assert stringify == "3 > 2 > 1"

def test_to_string_single_node(): 
  ll = LinkedList()
  ll.insert(1)  

  stringify = str(ll)

  assert stringify == "1"

def test_to_string_emtpy_list(): 
   ll = LinkedList() 

   stringify = str(ll)

   assert stringify == ""

def test_append(): 

  ll = LinkedList() 

  ll.insert(1)
  ll.insert(2)
  ll.insert(3)  

  ll.append(0) 

  #print(ll.head.next.next.value)
  assert ll.head.next.next.next.value == 0

def test_append_multiple(): 
  ll = LinkedList() 

  ll.insert(1)

  ll.append(2)
  ll.append(3)

  print(ll.head.next.value)
  assert ll.head.next.next.value == 3

def test_insert_before_at_begining(): 
  ll = LinkedList() 

  ll.insert(1) 
  
  ll.insert_before(1,0)

  assert ll.head.value == 0

def test_insert_before_at_mid(): 
  ll = LinkedList()

  ll.insert(1) 
  ll.insert(3) 

  ll.insert_before(1,2) 

  print(ll.head.next.value)
  assert ll.head.next.value == 2

def test_insert_after_at_mid(): 
  ll = LinkedList() 

  ll.insert(1) 
  ll.insert(3)

  ll.insert_after(3, 2) 

  print(str(ll))
  assert ll.head.next.value == 2

def test_insert_after_at_end(): 
  ll = LinkedList() 

  ll.insert(1) 
  ll.insert(2)
  
  ll.insert_after(1, 3)

  print(ll.head.next.next.value)
  assert ll.head.next.next.value == 3

"""
    Can successfully insert a node after the last node of the linked list
    """