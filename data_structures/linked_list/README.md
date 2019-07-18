# Singly Linked List

A singly linked list is a data-structure composed of nodes which have a next pointer and a value.

## Challenge

In this challenge, the goal was to write a singly linked list making use of pythons classes.

## Approach & Efficiency

I opted to create two classes, one for instantiating an empty LinkedList and holding the necessary methods, and one to create a Node and hold the pointer and the value. 
Over all, adding Nodes to this list will take O(1) time and space, and finding a specific node will be O(n) time and O(1) space. The to string method takes O(n) time and space.

## API

* class LinkedList - This class allows for the instantiation of a linked list with an empty head value utilizing the constructor. The LinkedList class has the following methods:

  * insert(value) - Insert takes in a value, and then instantiates a new Node as the head of the list with that value.

  * includes(value) - Includes takes in a value, and traverses the list via while loop looking for a node that has that value. If the value is found, includes will return true. If it is not found, includes will return false.

  * __str__(), str() - Linked Lists written via this class have a custom to string method that will print a representation of the list like this:

    '3 > 2 > 1'

* class Node - This class allows for the instantiation of a Node with a passed in value, and a next that can default to none or be passed in as well. This class is utilized in many of the methods on the LinkedList class.

## Challenge Summary for Linked List Insertion

Write a append, insert before, and insert after method to compliment the existing linked list class.

### Challenge Description for Linked List Insertion

Write the following methods on the linked list class: 
    * append - which takes in a value, inserts a new node of that value at the end of the list
    * insert before - which takes in a search value and a new value, finds the search value, and inserts a new node of the new value before the node of the search value 
    * insert after - which takes in a search value and a new value, finds the search value, and inserts a new node of the new value after the node of the search value


### Approach & Efficiency Of the Insertion Challenge for Linked List Insertion

    For all of these methods I opted to do my list traversals with while loops, checking the value of the current node against the insertion criteria. Because of this, they should all take O(n) time. After that, it was simply a matter of rearranging pointers to insert the new node, which means their space is O(1)! 

### Solution for Linked List Insertion

My partner for this challenge and I for this challenge each white-boarded out different functions, here is my solution to insert_after: 

![white board for insert before](../../assets/insert_node_before.jpg)

## Challenge Summary for kth from the End Search

Write a function that returns the value of the kth element from the end.

### Challenge Description for kth from the End Search

Traverse a linked list and find the node that is k from the end. Return the value of that node.

### Approach & Efficiency Of the Insertion Challenge for kth from the End Search

While I recognize it is not the most efficient solution, when pondering this problem I came up with a way to solve it utilizing two loops. The first loop is a classic list traversal, with an added counter keeping track of the length. The second loop goes to the kth node from the end, and then pulls that value to return.

### Solution for kth from the End Search

![white board for kth from the end](../../assets/kthFromTheEndSearch.jpg)
