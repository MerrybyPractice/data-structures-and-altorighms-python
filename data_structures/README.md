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
