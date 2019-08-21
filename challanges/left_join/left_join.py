from data_structures.hashtable.hashtable import Hashtable

def left_join(h1, h2): 

  lst_1 = pull_from_lst(h1)
  lst_2 = pull_from_lst(h2)

  return lst_1 & lst_2


def pull_from_lst(ht): 
  lst = [] 

  for item in ht.buckets: 

    if item.head: 
      
      pull_from_ll(ht, lst)

    else: 
      lst.append(item.head.value)


def pull_from_ll(ht, lst):
  
  current = ht.buckets.head

  while current: 

    if current.value['key']: 
      lst.append(current.value)

    current = current.next  

  return lst  
  


  

