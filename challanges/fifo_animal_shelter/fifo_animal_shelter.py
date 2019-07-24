from .animal import Animal
from data_structures.stacks_and_queues.stacks_and_queues import Queue


class Animal_Shelter(object): 

  def __init__(self):
    self.queue = Queue() 

  def fifo_animal_enqueue(self, animal): 
    self.queue.enqueue(animal)

  def fifo_animal_dequeue(self, pref = None): 
    current = self.queue.front
    if pref: 
      #pref exsists
      if current.value.type != pref: 
        #if pref exsists, not taking first
        while current.next.value.type != pref: 
          current = current.next
      else: 
        #if pref exsists, taking first
        return_value = current
        print(f'You have adopted {return_value.value.name} the {return_value.value.type}')
        return self.queue.dequeue()
      if current.next: 
        #if pref exsists, not taking first
          return_value = current.next.value
          current.next = current.next.next 
          print(f'You have adopted {current.next.value.name} the {current.next.value.type}')
          return return_value  
    else: 
      #if no pref exsists, taking first
      return_value = current
      print(f'You have adopted {current.value.name} the {current.value.type}')
      return self.queue.dequeue() 