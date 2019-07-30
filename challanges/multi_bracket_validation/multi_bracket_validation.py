from data_structures.stacks_and_queues.stacks_and_queues import Queue 

class MultiBrackatValidation: 
  
  def __init__(self): 
    self.queue = Queue()
    self.open_dict = {
      '[' : ']', 
      '{' : '}', 
      '(' : ')'
    }
    self.closed_dict = {
      ']' : '[', 
      '}' : '{', 
      ')' : '('
    }

  def multi_bracket_validation(self, input_string): 

    return_value = False

    arr = [c for c in input_string]
    
    for i in arr: 
      if i in self.open_dict.keys() or i in self.closed_dict.keys(): 
        self.queue.enqueue(i)
    
    count = [] 

    if self.queue.peek() in self.open_dict: 
      count.append(self.queue.dequeue()) 
    else: 
      print(self.queue.peek(), self.closed_dict.keys(), self.closed_dict[self.queue.peek()])
      if self.queue.peek() in self.closed_dict.keys() and self.closed_dict[self.queue.peek()] in count: 
        return_value = True

    return return_value          

