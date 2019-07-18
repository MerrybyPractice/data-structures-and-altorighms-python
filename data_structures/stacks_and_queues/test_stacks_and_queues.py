from data_structures.stacks_and_queues.stacks_and_queues import Stack 
from data_structures.stacks_and_queues.stacks_and_queues import Queue

def test_push(): 
  stack = Stack() 

  assert stack.push(1) == None

def test_push_top(): 
  stack = Stack() 

  stack.push(1) 
  print(stack.top)
  assert stack.top.value == 1

def test_push_multiple(): 
  stack = Stack() 

  stack.push(1) 
  stack.push(2)  
  stack.push(3) 

  assert stack.top.value == 3 
  assert stack.top.next.value == 2
  assert stack.top.next.next.value == 1

def test_pop(): 
  stack = Stack()

  stack.push(1)

  assert stack.pop() == 1

def test_pop_to_empty(): 
  stack = Stack() 

  stack.push(1) 
  stack.push(2)  
  stack.push(3) 

  assert stack.pop() == 3
  assert stack.pop() == 2
  assert stack.pop() == 1
  assert stack.pop() == None

def test_peek_empty(): 

  stack = Stack() 

  assert stack.peek() == None

def test_peek(): 

  stack = Stack() 

  stack.push(1) 

  assert stack.peek() == 1

def test_stack_exsists(): 

  stack = Stack() 

  assert stack.top == None
'''
Can successfully instantiate an empty queue
'''
def test_enqueue(): 
  queue = Queue() 

  assert queue.enqueue(1) == None
  assert queue.front.value == 1 

def test_enqueue_multiple(): 

  queue = Queue() 

  queue.enqueue(1)
  queue.enqueue(2) 
  queue.enqueue(3) 

  assert queue.front.value == 1 
  assert queue.front.next.value == 2
  assert queue.front.next.next.value == 3

def test_dequeue(): 

  queue = Queue() 

  queue.enqueue(1)
  queue.enqueue(2) 
  queue.enqueue(3)   

  assert queue.dequeue() == 1
  assert queue.dequeue() == 2
  assert queue.dequeue() == 3 

def test_peek_queue():   
  queue = Queue()

  queue.enqueue(1)

  assert queue.peek() == 1

def test_peek_queue_empty(): 
    queue = Queue()

    assert queue.peek() == None

def test_queue_exsists(): 
  queue = Queue() 

  assert queue.front == None 
