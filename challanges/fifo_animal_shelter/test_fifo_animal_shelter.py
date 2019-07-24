from challanges.fifo_animal_shelter.fifo_animal_shelter import Animal_Shelter
from challanges.fifo_animal_shelter.animal import Animal

def test_enqueue(): 
  shelter = Animal_Shelter() 

  cat = Animal("Bynx", "Cat")

  shelter.fifo_animal_enqueue(cat)

  assert shelter.queue.front.value == cat

def test_fifo_animal_dequeue(): 
  shelter = Animal_Shelter()
  
  cat = Animal("Salem", "Cat")

  shelter.fifo_animal_enqueue(cat)

  assert  shelter.fifo_animal_dequeue("Cat") == cat
