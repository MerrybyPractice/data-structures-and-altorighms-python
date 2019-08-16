# Hashtables

## Challenge

Implement a hashtable that can add values, retrieve values, and notify the user if a value is already stored in it.

## Approach & Efficiency

This hashtable implementation is composed of an array of linked lists. In this iteration, the linked lists are instantiated upon creation of the hashtable - however there is consideration of having them instantiate dynamically as each bucket is needed.

This implementation has a space complexity of O(N). The time complexity is addressed on each function in the API section.

## API

Hashtable():
  
  This class instantiates with an array of 1024 linked lists, ready to take in hashed key/value pairs.

.hash(key):

  O(n)

  Hash takes in a key and generates a hashed index for it to reside at in the table. While this method was created as a helper function for the class, it has been made publicly avaliable so that users may have access to it as they expand on and work with this hashtable.

.add(key, value):

  On average, the space complexity here will be O(1)

  Add takes in a key and a value. It calls Hash on the key, and then stores both the key and value in a dict at that index of the hashtable.

.get(key):

  Given that get uses a while loop for list traversal, the space complexity will be O(n)

  Get takes in a key, locates the hashed index of that key, and searches to see if it is currently stored there. If it is, get will return that value. If it is not, get returns None. 

.contains(key):

  Given that get uses a while loop for list traversal, the space complexity will be O(n)

  Contains takes in a key, locates the hashed index of that key, and searches to see if it is currently stored there. If it is, get will return True. If not, it will return False.
