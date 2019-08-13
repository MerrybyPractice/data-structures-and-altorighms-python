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

Insertion sorts perform best with with smaller data sets that are coming in partially sorted. It may also be a good choice when you require an in-place sort, or a stable sort -- depending on other constraints of course.

Space Complexity: O(1)
Time Complexity: O(N^2)

### Should this Algorithm be stable?

So, what is a stable algorithm and why do I care? In a stable sort, identical values are not swapped when encountered. In an unstable sort they are. Fundamentally, it is typically an efficiency thing. You do not want to be taking additional steps you do not need to get the same result. However, there may be other considerations that will favor a stable sort over an unstable one.

## Diagram

[VisualAlgo Insertion Sort](https://visualgo.net/bn/sorting?slide=8)

![Tonal Insertion Sort from Timo Bingmann](https://www.youtube.com/watch?v=8oJS1BMKE64)

## Algorithm

  1. Instantiate a key holding variable
  2. Select the left most unsorted element as a key
  3. Move your key to the sorted sub-collection, ie. the left most portion of the array. 
  4. Reassign the key as the next left most unsorted element. 
  5. Check where in the sorted sub-collection the key would fit. 
    * Starting from the right, see if the key is larger than or smaller than each element in the sorted sub-collection. 
    * When you find where it fits, insert the key value there, shifting the rest. 
  6. Perform 4-5 until entire array is sorted.  

## Pseudocode

## Readings and References

### Watch

[AlgoRythmics performs the Insertion Sort](https://www.youtube.com/watch?v=ROalU379l3U)
[Geeks for Geeks Insertion Sort](https://www.youtube.com/watch?v=OGzPmgsI-pQ)

### Read

[Khan Academy Insertion Sort](https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort)
[Study Tonight Insertion Sort](https://www.studytonight.com/data-structures/insertion-sorting)


### Bookmark

[HackerEarth Insertion Sort Visualizer](https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/)

[Big O Cheatsheet](https://www.bigocheatsheet.com/)
