from data_structures.linked_list.linked_list import LinkedList 

class Hashtable: 

  def __init__(self): 

    self.buckets = [LinkedList for i in range(1024)]

