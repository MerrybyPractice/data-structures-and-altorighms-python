import pytest

from sorting_algorithims.quick_sort.quick_sort import quick_sort

def test_quick_sort(): 

  arr = [3,5,6,2,9]
  right = (len(arr) -1) 

  assert quick_sort(arr, 0, right) == [2,3,5,6,9]

def test_one(): 

  arr = [3]

  assert quick_sort(arr, 0, len(arr)-1) == [3] 

def test_two(): 

  arr = [4,2]

  assert quick_sort(arr, 0, len(arr)-1) == [2,4] 

def test_two_ordered(): 

  arr = [2,4]

  assert quick_sort(arr, 0, len(arr)-1) == [2,4]        
