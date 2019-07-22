from data_structures.stacks_and_queues.stacks_and_queues import Stack

class Pseudoqueue: 

  def __init__(self): 
    self.back = Stack()
    self.front = Stack() 

  def enqueue(self, value):
    try: 
      while self.front: 
        moving_node = self.front.pop()
        self.back.push(moving_node.value)
    except AttributeError: 
      print('Front is Empty')    

    self.back.push(value)
    print("back top",self.back.top.value)

    try:
      while self.back: 
        moving_node = self.back.pop() 
        self.front.push(moving_node.value)
        print("front top",self.front.top.value)  
    except AttributeError: 
      print('Back is Empty')    

  def dequeue(self): 
    pass  
