from challanges.max_tree.max_tree_value import max_tree_value
from data_structures.tree.tree import BinaryTree
from data_structures.tree.tree import Node
import pytest

@pytest.fixture
def ent():
  bt = BinaryTree()

  #root 
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
  bt.root.right.right.right = Node(18)   

# root right left child 
  bt.root.right.left.left = Node(12)  
  bt.root.right.left.right = Node(14)

  return bt

def test_happy_path(ent): 
  
  assert max_tree_value(ent) == 18

def test_empty_tree(): 

  treebeard = BinaryTree() 

  assert max_tree_value(treebeard) == None  

