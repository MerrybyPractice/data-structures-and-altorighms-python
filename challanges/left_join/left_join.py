from data_structures.hashtable.hashtable import Hashtable

def left_join(h1, h2): 

  return_list = [] 

  for word in h1: 

    entry = [word, h1[word], h2.get(word)]

    return_list.append(entry)

  return return_list

  

