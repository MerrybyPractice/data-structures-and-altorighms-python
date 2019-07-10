from .array_shift import insert_shift_array

def test_insert_shift_array_exsist(): 
  assert insert_shift_array([1],2)

def test_insert_shift_array_happy_path(): 
  
  expected = [2, 4, 8, 3, 6]
  actual = insert_shift_array([2,4,3,6], 8)

  assert expected == actual

def test_insert_shift_array_len_three(): 
  
  expected = [9, 5, 0, 7]
  actual = insert_shift_array([9, 0, 7], 5)

  assert expected == actual  

def test_insert_shift_array_len_two(): 
  
  expected = [7, 9, 3]
  actual = insert_shift_array([7, 3], 9)

  assert expected == actual   

def test_insert_shift_array_len_one(): 
  
  expected = [8, 3]
  actual = insert_shift_array([3], 8)

  assert expected == actual

def test_insert_shift_array_empty(): 
  
  expected = [7]
  actual = insert_shift_array([], 7)

  assert expected == actual 