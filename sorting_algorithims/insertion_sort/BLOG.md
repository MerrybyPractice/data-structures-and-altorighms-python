# Blog Notes: Insertion Sort

Insertion sort is a O(n) in place sorting algorithm that mimics sorting a hand of cards in hand.

By keeping all sorted items in a set apart, insertion sort minimizes resorting. Additionally, because it is based on a real world problem, it is easy to conceptualize when working with!

## Learning Objectives

- The Basics of an Insertion Sort! Basic structure of an Insertion Sort Algorithm

- So, when to insert? When is it a good idea to use Insertion sort?

- Should this Algorithm be stable? What is a Stable Sorting Algorithm?

## Information Flow

### The Basics of an Insertion Sort!

1. The array to be sorted. You can sort pretty much any collection. In this example, we will be sorting an array. However, with a little creativity, you can set yourself up to sort all kinds of data structures.

2. A key. This is dynamic, in that it will change over the course of our sort. The key is simply the value we are currently evaluating. You could call it current, or value, or to_be_sorted or anything else you wanted.

3. The sorted collection, rather the already sorted sub collection of values you no longer have to worry about! These are the items you have compared, know where they go, and are _inserting_ new values in between.

How do these all fit together? Good question! 

Do you have a deck of cards, or dice, or anything physical you can order? If so grab that now! 

First, do you have anything in your sorted sub-collection? No? Good. 

Lets pick our first key. Place your objects in front of you, or in hand, in a single line. Right now, order does not matter - in fact the more shuffled the better this demonstration will work! For our first key, we will be picking the object on the farthest left. To start us off, lets just move that into the sorted collection. Boom, one item sorted. Now, lets look at the next item to the left, place that where it goes next to the first one. Keep going until everything is moved into the sorted sub collection.

And thats it, a basic physical representation of insertion sort. You simply keep _inserting_ your items into a sorted sub collection until everything is accounted for!

### So, when to insert?



### Should this Algorithm be stable?

## Diagram

Include your “Visual” here

## Algorithm

Describe in detail how the algorithm works. Include small code snippets to possibly support the points

## Pseudocode

## Readings and References

### Watch

### Video

### Read

[Khan Academy Insertion Sort](https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort)
[Study Tonight Insertion Sort](https://www.studytonight.com/data-structures/insertion-sorting)

Article 2
### Bookmark

[HackerEarth Insertion Sort Visualizer](https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/)

[Big O Cheatsheet](https://www.bigocheatsheet.com/)
