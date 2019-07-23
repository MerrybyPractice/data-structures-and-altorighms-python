from data_structures.stacks_and_queues.stacks_and_queues import Stack

class Pseudoqueue: 

  def __init__(self): 
    self.back = Stack()
    self.front = Stack() 

  def enqueue(self, value):
    print("pushing ", value)
    try: 
      while self.front.top != None: 
        self.back.push(self.front.pop())
        # print('xxxx')
        # print(self.back.top.value)
        # print(self.back.top.next)
    except AttributeError: 
      print('Front is Empty')    

    self.back.push(value)
    # print(self.back.top.value)

    try:
      
      while self.back.top != None: 
        # print(self.back.top.value)
        self.front.push(self.back.pop())
        # print('-----------')
    except AttributeError: 
      print('Back is Empty')
    # print('top: ', self.front.top.value)

  def dequeue(self): 
   return self.front.pop()
