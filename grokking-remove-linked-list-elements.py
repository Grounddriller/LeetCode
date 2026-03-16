from ds_v1.LinkedList.LinkedList import ListNode
            
def remove_elements(head, k):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == k:
            current.next = current.next.next
        else: current = current.next
        
    return dummy.next
