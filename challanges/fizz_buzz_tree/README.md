# Fizz Buzz Tree 7/29/19

Given a binary tree, write a function that performs the Fizz Buzz game on it. 

## Challenge

Taking in a binary tree, change any modulo 3 values to the word "Fizz", any modulo 5 values to the word "Buzz", and any that are modulo by 3 and 5 into "FizzBuzz." 

## Approach & Efficiency

As recursive traversals are the best way to get through trees, I employed a post order one to my benefit here. Before the traversal, this code checks for %3, %5, and %3 and %5 values and replaces them with their respective words. At the end, it returns the completed tree. Its that simple!

## Solution

![merge_lists](../../assets/Fizz_Buzz_Tree)
