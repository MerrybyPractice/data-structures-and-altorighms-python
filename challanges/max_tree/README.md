# Find the Max Value in a Binary Tree 7/31/19

Given a binary tree as input, return the max value. 

## Challenge

Traverse over a binary tree comparing node values. Once finished, return the maximum value.

## Approach & Efficiency

In this challenge, I opted to instantiate a holding value with the root value and then traverse recursively. At each node, I compare the node value against the holding value, and assign the node value to the holding value if the node value evaluates as larger. At the end, the holding value is returned and should contain the largest value in the tree! This is O(h) for time, and O(1) for space!

## Solution

![merge_lists](../../assets/max_tree.jpeg)
