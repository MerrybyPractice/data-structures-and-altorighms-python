# Blog Notes: Quick Sort

Quicksort is an in place divide and conquer sort that uses partitioning to order elements in a collection on average more efficiently than merge sort.

## Learning Objectives

Parts of a Quicksort? 
  * Pivot
  * Partition 

## Parts of a Quicksort

### Pivot 

A Carefully selected element in the collection around which a portion of the sort will happen. By the time an operation is done at a specific pivot, all of the elements in the collection to the left of the pivot will be smaller than it, and all of the elements to the right of the pivot will be larger than it. However _these elements will only be larger or smaller relative to the pivot, not necessarily each other_.

### Partition 

The process by which elements are moved around a pivot. 

## Diagram

[Quick Sort AudioVisuaization by Timo Bingmann](https://www.youtube.com/watch?v=8hEyhs3OV1w)

## Algorithm

Input: Collection, first index, last index 
Output: Collection (sorted)

1. Find the median (or closest whole number) between the first and last index of the array and set it as the pivot. 
2. Set left pointer at index 0 and right pointer at index 0-1 
3. Check the value at each pointer, if said value is on the correct side of the pivot:
    - left pointer increments 
    - decrements pointer decrements 
4. When a pointer finds an element that it is out of place (greater than pivot on the left, less than on the right) it stops 
until the other pointer also finds an element that is out of place. 
5. When both pointers have found an element that is out of order, they swap them. 
6. Once both pointers are able to move through the array and intersect without swapping the array counts as sorted. 
7. This is called recursively, which manages all of the heavy lifting a loop or other control flow method might in this 
circumstance.

## Readings and References

### Watch

[AlgoRythmics Quicksort](https://www.youtube.com/watch?v=ywWBy6J5gz8)

### Read

[A Quick Explanation of Quick Sort by Karuna Sehgal on Medium](https://medium.com/karuna-sehgal/a-quick-explanation-of-quick-sort-7d8e2563629b)

[Base CS Pivoting to Understand Quicksort by Vaidehi Joshi](https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313)
### Bookmark

[Kvick Sört part of the IDEA Project by Sándor P. Fekete and Sebastian Morr](https://idea-instructions.com/quick-sort/)
