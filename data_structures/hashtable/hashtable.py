from data_structures.linked_list.linked_list import LinkedList as ll

class Hashtable: 

  def __init__(self): 

    self.buckets = [ll() for i in range(1024)]

  def hash(self, key): 
    unicode_sum = sum([ord(char) for char in key])

    prime = 997

    idx = unicode_sum * prime % len(self.buckets)

    return idx

  def add(self, key, value): 

    idx = self.hash(key)

    bucket = self.buckets[idx] 

    bucket.insert({'key': key, 'value': value})

  def get(self, key): 

    idx = self.hash(key) 

    bucket = self.buckets[idx]  
      
    current = self.buckets[idx].head 

    while current: 
      
      if current.value['key'] == key: 
        return current.value['value']
      else: 
        current = current.next  

    return None

  def contains(self, key): 

    idx = self.hash(key) 

    bucket = self.buckets[idx]  
      
    current = self.buckets[idx].head 

    while current: 
      
      if current.value['key'] == key: 
        return True
      else: 
        current = current.next  

    return False    
