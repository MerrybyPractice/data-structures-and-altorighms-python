from data_structures.hashtable.hashtable import Hashtable
from challanges.left_join.left_join import left_join
import pytest

def test_left_join(): 
  h1 = Hashtable()
  h1.add("2",2)
  h1.add("3",3)

  h2 = Hashtable()
  h2.add("2",2)
  h2.add("4",4)

  assert left_join(h1, h2) == [{2,2}]