# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:
            nextNodepair = current.next.next
            second = current.next

            second.next = current
            current.next = nextNodepair
            prev.next = second

            prev = current
            current = nextNodepair

        return dummy.next
