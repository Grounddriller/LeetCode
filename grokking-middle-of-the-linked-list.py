from ds_v1.LinkedList.LinkedList import ListNode

def get_middle_node(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
