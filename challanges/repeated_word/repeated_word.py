from challanges.repeated_word.abc_dict import ABC_dict
from data_structures.hashtable.hashtable import Hashtable

def repeated_word(strs): 

  strs = strs.lower()

  for ch in strs: 
    if ch not in ABC_dict: 
      strs.replace(ch, '')

  str_lst = strs.split(" ")

  ht = Hashtable()

  for string in str_lst: 
    if ht.contains(string): 
      return string
    else: 
      ht.add(string, string)  

  return None    


