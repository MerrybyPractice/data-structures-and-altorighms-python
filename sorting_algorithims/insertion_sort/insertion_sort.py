
def insertion_sort(arr): 

  for i in range(0, len(arr)-1 ): 
    j = i-1
    temp = arr[i] 

    while j >= 0 and temp < arr[j]: 
      arr[j+1] = arr[j] 
      j = j-1 

      arr[j+1] = temp

  return arr     



