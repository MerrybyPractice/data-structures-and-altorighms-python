# Merge 2 Linked Lists 7/17/19

Write a function that takes in two linked lists, and combines them into one before returning the head.

## Challenge

Given two passed in lists, reassign their pointers until there is one continuous list. Then, return a reference to the head of this new list.

## Approach & Efficiency

In this challenge, I started off by creating two current nodes to keep track of the floating nodes and a runner to help reassign pointers across the list. I reassigned the head pointers before jumping into a while loop, which kept the runner and current's advancing until one of the lists runs out. Then, the head of the first list, now the head of the whole list, is returned. This will be O(n) time, and O(1) space!

## Solution

![merge_lists](../../assets/merge_lists)
