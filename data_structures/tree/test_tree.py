from tree import Node
from tree import BinaryTree
import pytest 

@pytest.fixture
def ent():
  bt = BinaryTree()

  #root 
  bt.root = Node(10)
  root_left = bt.root.left
  root_left = Node(5)
  root_right = bt.root.right 
  root_right = Node(15)

  #root left child 

  rl_left = root_left.left 
  rl_left = Node(3)
  rl_right = root_left.right 
  rl_right = Node(7)

# root left right child 

  rlr_left = rl_right.left 
  rlr_left = Node(6)
  rlr_right = rl_right.right
  rlr_right = Node(8)

# root left left child 

  rll_left = rl_left.left 
  rll_left = Node(2) 
  rll_right = rl_left.right
  rll_right = Node(4)

# root right child 

  rr_left =  root_right.left 
  rr_left = Node(17)
  rr_right = root_right.right 
  rr_right = Node(13) 

# root right right child 

  rrr_left = rr_right.left
  rrr_left = Node(14) 
  rrr_right = rr_right.right
  rrr_right = Node(12)   

# root right left child 

  rrl_left = rr_left.left
  rrl_left = Node(18)  
  rrl_right = rr_left.right 
  rrl_right = Node(16)

  return bt

def test_node_exsists(): 
  assert Node(0)

def test_tree_exsists(): 
  assert BinaryTree()

@pytest.mark.skip('need to figureout fixtures')
def test_inorder_traversal(ent): 

  assert ent.in_order_traversal() == [2,3,4,5,6,7,8,10,12,13,14,15,16,17,18]

