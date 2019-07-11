from .array_binary_search import binary_search

def test_array_binary_search_exsist(): 

  expected = 0

  lst = [4]
  key = 4
  actual = binary_search(lst, key)
  assert expected == actual

def test_array_binary_search_happy_path(): 
  expected = 2 

  lst = [1,2,5,7,8,10]
  key = 5

  actual = binary_search(lst, key)

  assert expected == actual

def test_array_binary_search_uneven_array(): 
  expected = 0

  lst = [15,45,89]
  key = 15

  actual = binary_search(lst, key)

  assert expected == actual

def test_array_binary_search_empty_array(): 
  expected = -1 

  lst = []
  key = 99

  actual = binary_search(lst, key)

  assert expected == actual 

def test_array_binary_search_not_in_array(): 
  expected = -1

  lst = [55,78,90,104]
  key = 1

  actual = binary_search(lst, key)

  assert expected == actual