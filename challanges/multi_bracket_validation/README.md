# Multi Bracket Validation

Write a function that returns a boolean telling if a string with brackets is balanced or not.

## Challenge

Given a string that contains brackets ((,),{,},[,]), write a function that will check if they are balanced and return a boolean. 

## Approach & Efficiency

I opted to use a list comprehension to divide my string into individual characters, and enqueue only the brackets into a queue. This was done by checking them against dictionaries containing brackets, and not enqueueing characters that were not in those dictionaries. After that queue has all the brackets in the string in it, I check them for opening brackets and push open brackets and close brackets that match opening brackets already in the array to an array. If at any point there is a confounding closing bracket, the return value is set to false and returned. If not, it is set to true. If this finishes, everything hops out of the if block and returns true. This is O(N) for both time and space.

## Solution

![mulit_bracket_validation](../../assets/miltiBracketValidation.jpeg)
