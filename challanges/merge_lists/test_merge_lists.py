from data_structures.linked_list.linked_list import LinkedList
from .merge_lists import merge_lists

def test_merge_lists(): 

  ll_1 = LinkedList() 
  
  ll_2 = LinkedList() 

  ll_1.insert(1) 
  ll_1.insert(3) 
  ll_1.insert(5) 

  ll_2.insert(2) 
  ll_2.insert(4) 
  ll_2.insert(6) 

  assert merge_lists(ll_1, ll_2).value == 5