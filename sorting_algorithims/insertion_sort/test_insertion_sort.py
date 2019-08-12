import pytest 
from sorting_algorithims.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_exsists(): 
  assert insertion_sort([1,3,4])

def test_happy_path(): 
  
  arr = [1,4,6,3,5,7]

  assert insertion_sort(arr) == [1,3,4,5,6,7]

def test_all_same(): 
  
  arr = [7,7,7,7,7]

  assert insertion_sort(arr) == [7,7,7,7,7]

def test_one(): 
  
  arr = [3] 

  assert insertion_sort(arr) == [3]

def test_already_sorted(): 
  
  arr = [1,3,5,7,9] 

  assert insertion_sort(arr) == [1,3,5,7,9] 

def test_with_negatives(): 
  
  arr = [3, -1, 0, -5, 6, 8, 9]

  assert insertion_sort(arr) == [-5, -1, 0, 3, 6, 8, 9]
