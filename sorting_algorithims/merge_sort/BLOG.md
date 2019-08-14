# Blog Notes: Merge Sort

A Merge Sort is a recursive divide and conquer algorithm that breaks a collection down into its smallest components and then sorts as it rebuilds into a whole.   

## Learning Objectives

1. Divide and Conquer Algorithms 
2. Parts and functions of a merge sort 
3. Understanding the benefits and trade offs of merge sort

## Divide and Conquer Algorithm

  Divide: This approach to problem solving begins by taking the problem apart, down to bits small enough you know how to handle them.

  Conquer: Im sure you have been told to think of recursion in similar terms. Finding the smallest possible problem you need to solve. Divide and Conquer Algorithms will typically use recursion for the conquer step,that is, they will recursively solve the problem once it has been broken down into the smallest possible bits. 

  Combine: Either as a by product of recursing, or as an intentional step, combine the smaller solved parts into a larger solved whole.

  This type of algorithm is found all over, however today we will be focusing on one example - the merge sort. 

## Parts and Function of Merge Sort

### As a Divide and Conquer Algorithm

* Divide: Break your collection down into single element sub collections. 
* Conquer: Divide, recursively.
* Combine: After the recursive divide calls, call the merge function so that it is hit on the way back up the stack. 

In many traditional implementations of this the divide and merge functions are distinct, with the merge function being called inside divide. So, what needs to be handled in each? 

### Divide: 

* Find the mid point of your collection. 
* Split it into two sub collections on that point. 
* Call divide on each sub collection. 
* Call merge 
* Return (if necessary for your use case)

### Combine: 

* Check the size of your collection
* If two or more, compare where they go in the existing sorted collection and insert them. 
* If only one, compare where it goes in existing sorted collection and insert it there. 

## Diagram
![IDEA a project by Sandor P. Fekete and Sebastian Morr](idea-instructions.com/merge-sort/)

## Algorithm

1. Input: 
    - Arr - Our Sort needs to take into a collection, for ease this should be an Array. 
        - However, if the students feel strongly else wise run with it. (As with the Insertion sort lecture in this series, 
        the goal is for them to feel ownership over this process just as much it is providing an accurate Algorithm. Both are vital.) 
    - first - Index of 1st Element in the collection
    - last - Index of Last Element in the collection 
3. Find the Mid Point 
    - mid = (first+last)/2 
2. Recursion: 
    - Call two different instances of MergeSort: 
        - first half: MergeSort(arr, first, mid)
        - second half: MergeSort(arr, mid+1, last)
3. Merge 
    - Write the merge function separately to be called within merge sort 
    1. Input: 
        - Arr 
        - first 
        - mid
        - last 
    2. Create a new list to merge into (language/collection specific step) 
    3. Compare the first element of each collection to be merged, place the smaller first. 
        - traverse through the rest of the collection following the same procedure
    4. when finished with 2 initial collections, return sorted collection 


## Pseudocode

Sort 
 
    Sort(Arr, first, last) - no return 

    // find the mid point 
    mid = (first+last)/2 

    //Recursion 
    Sort(Arr, first, mid)
    Sort(Arr, mid+1, last)
    
    //Merge
    
    Merge(Arr, first, mid, last)


Merge 

    Merge(Arr, first, mid, last) - no return 
    
    //create a holding array for the merge, one larger than the size of the two arrays to be combined 
    holdingArray [last-first +1] 
    
    //create variables to hold the index we are at in each array
    
    i = first;  //array 1
    j = mid+1;  //array 2
    k = 0;      //holdingArray
    
    while i is smaller than mid and j is smaller than last 
        if i is less than or equal to j 
            set the value of k as the value of i 
            increment i and k 
        else 
            set the value of k as the value of j 
            increment j and k 
    
    //these line are in place incase array 1 and array 2 are mismatched in size 
        
    while i is smaller than mid 
        the value of k is equal to the value of i 
        increment i and k 
        
    while j is smaller than last 
        the value of k is equal to the value of j 
        increment j and k 
    
    //finally copy the holding array back over to the original array 
    
    for loop i equals first, less than end, increment 
        Arr at index i = holding array at index of (i - first)
        

## Readings and References

### Watch

[Merge Sort Audovisualization by Timo Bingmann](https://www.youtube.com/watch?v=ZRPoEKHXTJg)
[Geeks for Geeks on Merge Sort](https://www.youtube.com/watch?v=JSceec-wEyw)

### Read

[Geeks for Geeks Divide and Conquer Algorithm](https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/)
[Geeks for Geeks Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
[Interview Bit Merge Sort](https://www.interviewbit.com/tutorial/merge-sort-algorithm/)
