from challanges.fizz_buzz_tree.fizz_buzz_tree import Fizz_Buzz_Tree
from data_structures.tree.tree import Node
from data_structures.tree.tree import BinaryTree
import pytest

@pytest.fixture
def happy_path(): 
  bt = BinaryTree

  bt.root = Node(10)
  bt.root.left = Node(5)
  bt.root.right = Node(15)

  #root left child 

  bt.root.left.left = Node(3)
  bt.root.left.right = Node(7)

# root left right child 

  bt.root.left.right.left = Node(6)
  bt.root.left.right.right = Node(8)

# root left left child 

  bt.root.left.left.left = Node(2) 
  bt.root.left.left.right = Node(4)

# root right child 

  bt.root.right.left = Node(13)
  bt.root.right.right = Node(17) 

# root right right child 

  bt.root.right.right.left = Node(16) 
  bt.root.right.right.right = Node(20)   

# root right left child 
  bt.root.right.left.left = Node(12)  
  bt.root.right.left.right = Node(14)

  return bt

def test_happy_path_root(happy_path): 

  assert happy_path.root.value == 'Buzz'

def test_happy_path_fizz(happy_path): 

  assert  happy_path.root.left.right.left.value == 'Fizz' 

def test_happy_path_fizzbuzz(happy_path): 

  assert happy_path.root.right.value == 'FizzBuzz'

def test_happy_path_buzz(happy_path): 
  
  assert happy_path.root.left.value == 'Buzz'

def test_happy_path_neither(happy_path): 
  
  assert happy_path.root.right.left.right.value == 14





