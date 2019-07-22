from challanges.queue_with_stacks.queue_with_stacks import Pseudoqueue

def test_pesudoqueue(): 
  pseudoqueue = Pseudoqueue()

  assert pseudoqueue.front.top == None
  assert pseudoqueue.back.top == None


def test_enqueue(): 
  pseudoqueue = Pseudoqueue()

  pseudoqueue.enqueue(1) 

  assert pseudoqueue.front.top.value == 1
  assert pseudoqueue.back.top == None

def test_dequeue(): 
  pass
  