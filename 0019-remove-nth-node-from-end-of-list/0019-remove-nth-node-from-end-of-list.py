# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list1 = []
        current=head
        while current:
            list1.append(current.val)
            current=current.next
        length=len(list1)
        index=length-n
        list1.pop(index)

        tempNode = ListNode(0)
        current = tempNode
        for i in list1:
            current.next = ListNode(i)
            current = current.next
        return tempNode.next