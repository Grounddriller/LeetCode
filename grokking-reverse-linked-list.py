from ds_v1.LinkedList.LinkedList import ListNode

def reverse(head):
    
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev
