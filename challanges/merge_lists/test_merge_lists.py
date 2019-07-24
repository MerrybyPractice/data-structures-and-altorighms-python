from data_structures.linked_list.linked_list import LinkedList
from .merge_lists import merge_lists
import pytest

@pytest.mark.skip('refactor')
def test_merge_lists(): 

  ll_1 = LinkedList() 
  
  ll_2 = LinkedList() 

  ll_1.insert(1) 
  ll_1.insert(3) 
  ll_1.insert(5) 

  ll_2.insert(2) 
  ll_2.insert(4) 
  ll_2.insert(6) 

  

  test_list_head = merge_lists(ll_1, ll_2)

  assert test_list_head.value == 5
  assert test_list_head.next.value == 6
  assert test_list_head.next.next.next.next.value == 2




 
  