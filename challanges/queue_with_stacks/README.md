# A Queue with 2 Stacks

Mimic the functionality of a queue utilizing two stacks.

## Challenge

Use two stacks to create a structure that functions on the FIFO principal. It needs to be able to enqueue and dequeue, and can utilize all the . 

## Approach & Efficiency

In this challenge, I started off by creating two current nodes to keep track of the floating nodes and a runner to help reassign pointers across the list. I reassigned the head pointers before jumping into a while loop, which kept the runner and current's advancing until one of the lists runs out. Then, the head of the first list, now the head of the whole list, is returned. This will be O(n) time, and O(1) space!

## Solution

![psudoqueue](../../assets/psuedoque.jpeg)
