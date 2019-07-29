# Trees

A Binary Tree with a Binary Search Tree that extends it.

## Challenge

Write a binary tree class and its complimentary node class. Then, extend that with a binary search tree class the implements the a few additional methods.

## Approach & Efficiency

After writing my recursive traversals for the binary tree, I opted to base every other method I wrote on these classes. Most of these methods are O(n) for time and O(1) for space.

## API

* Binary Tree 
  - BinaryTree()
    - In_Order_Traversal() 
    - Post_Order_Traversal() 
    - Pre_Order_Traversal()
* Binary Search Tree
  - BinarySearchTree() 
    - Contains() 
    - Add()    