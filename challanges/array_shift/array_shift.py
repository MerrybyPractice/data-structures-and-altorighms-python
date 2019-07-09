def insert_shift_array(list, val): 
  
  i = int(len(list)/2)
  front = list[0:i:] 
  
  back = list[i::]
  
  front.append(val) 
  front.extend(back) 

  return(front)
  
  
print(insert_shift_array([2,4,3,6], 8))  