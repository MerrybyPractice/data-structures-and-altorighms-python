def binary_search(lst, key): 
  mid = len(lst)//2 
  try: 
    if lst[mid] == key: 
      return lst.index(lst[mid])
    elif lst[mid] > key: 
      return binary_search(lst[:mid], key) 
    elif lst[mid] < key: 
      return binary_search(lst[mid:], key) + len(lst[:mid])
  except IndexError: 
    return -1  