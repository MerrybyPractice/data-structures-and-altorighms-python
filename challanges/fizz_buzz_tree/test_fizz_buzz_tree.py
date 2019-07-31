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
  Fizz_Buzz_Tree(bt)
  return bt

@pytest.fixture
def all_threes(): 
  bt = BinaryTree() 

  bt.root = Node(9) 

  bt.root.right = Node(15)
  bt.root.left = Node(3)
  bt.root.right.right = Node(18)
  bt.root.right.left = Node(12)
  bt.root.left.right = Node(6)

  return bt

@pytest.fixture
def all_fives(): 
  bt = BinaryTree() 

  bt.root = Node(20) 

  bt.root.right = Node(30)
  bt.root.left = Node(15)
  bt.root.right.right = Node(35)
  bt.root.right.left = Node(25)
  bt.root.left.left = Node(10)
  bt.root.left.left.left = Node(5)

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
def test_all_threes(all_threes): 
  Fizz_Buzz_Tree(all_threes) 

  assert all_threes.root.value == "Fizz" 
  assert all_threes.root.right.value == "FizzBuzz"
  assert all_threes.root.left.value == "Fizz"
  assert all_threes.root.right.right.value == "Fizz"
  assert all_threes.root.right.left.value == "Fizz"
  assert all_threes.root.left.right.value == "Fizz"

def test_all_fives(all_fives): 

  Fizz_Buzz_Tree(all_fives)

  assert all_fives.root.value == "Buzz" 
  assert all_fives.root.right.value == "FizzBuzz"
  assert all_fives.root.left.value == "FizzBuzz"
  assert all_fives.root.right.right.value == "Buzz"
  assert all_fives.root.right.left.value == "Buzz"
  assert all_fives.root.left.left.value == "Buzz"
  assert all_fives.root.left.left.left.value == "Buzz"

def test_empty(): 

  bt = BinaryTree() 

  with pytest.raises(AttributeError):
    assert Fizz_Buzz_Tree(bt) == None




