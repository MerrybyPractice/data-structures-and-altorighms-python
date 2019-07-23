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
  pseudoqueue = Pseudoqueue() 

  pseudoqueue.enqueue(1) 
  dequeue = pseudoqueue.dequeue()

  assert dequeue == 1

def test_enqueue_multiple(): 
    pseudoqueue = Pseudoqueue()

    pseudoqueue.enqueue(1) 
    pseudoqueue.enqueue(2) 
    pseudoqueue.enqueue(3) 
    pseudoqueue.enqueue(4)

    assert pseudoqueue.front.top.value == 1
    assert pseudoqueue.front.top.next.value == 2
    assert pseudoqueue.back.top == None

  