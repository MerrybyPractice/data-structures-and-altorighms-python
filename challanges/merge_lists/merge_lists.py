from data_structures.linked_list.linked_list import LinkedList

def merge_lists(ll_1, ll_2):     
    current_1 = ll_1.head 
    current_2 = ll_2.head

    runner = ll_2.head 

    current_1 = current_1.next    
    ll_1.head.next = current_2 
    ll_2.head.next = current_1 

    while current_1 and current_2: 

      current_1 = current_1.next 
      runner.next = current_2
      runner = runner.next

      current_2 = current_2.next
      runner.next = current_1
      runner = runner.next

    return ll_1.head  