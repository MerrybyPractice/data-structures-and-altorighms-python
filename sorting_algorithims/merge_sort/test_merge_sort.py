import pytest
from merge_sort import mergesort

def test_mergesort(): 

  assert mergesort([1,5,4,7,3]) == [1,3,4,5,7]
