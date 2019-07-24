from .animal import Animal
from data_structures.stacks_and_queues.stacks_and_queues import Queue


class Animal_Shelter(object): 

  def __init__(self):
    self.queue = Queue() 

  def fifo_animal_enqueue(self, animal): 
    self.queue.enqueue(animal)

  def fifo_animal_dequeue(self, pref = None): 
    
    

    if pref: 
      pass
    