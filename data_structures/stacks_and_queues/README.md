# Stacks and Queues

A Stack class and a Queue class.

## Challenge

Utilizing the previously created Linked List and Node classes, implement a Stack and a Queue class that reorganize how information is accessed out of the Linked List.

The end user should have no awareness that the Stack and Queue classes are based off of a Linked List.

## Approach & Efficiency

I opted to make use of the properties and methods my linked list implementation already had, namely head, next, value, append, and insert. By declaring the top or front of the stack or queue respectively to be the head of the list, I was able to manipulate the nodes just like I would in a linked list. Most operations take O(1) time, except for enqueue, which utilizes append and is O(n). They are all O(1) for space.

## API

* Stack

    Properties:
      Top
      _list

    Methods:
      Push(value): returns None
      Pop(): returns and removes top value
      Peek(): returns top value

* Queue

    Properties:
      Front
      _list

    Methods:
      Enqueue(value): returns None
      Dequeue(): returns and removes front value
      Peek(): returns the front value
