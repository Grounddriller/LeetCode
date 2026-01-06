# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode(0) #False starting node
        curr = dummyHead #pointer to the lastest node
        carry = 0 #Stores carry values
        while l1 != None or l2 != None or carry != 0: #makes sure to go through every digit in the lists
            l1Val = l1.val if l1 else 0 #If the list still has a node, use its digit, else treat it like digit 0.
            l2Val = l2.val if l2 else 0 #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            columnSum = l1Val + l2Val + carry #ones column sum
            carry = columnSum // 10 #next digit carry
            newNode = ListNode(columnSum % 10) #digit stored in the current output node
            curr.next = newNode #appends new node to the result list
            curr = newNode #moves curr foward in the list fo we can append the next digit
            l1 = l1.next if l1 else None #move to the next node if l1 exists 
            l2 = l2.next if l2 else None #move to the next node if l2 exists 
        return dummyHead.next #Ruturns final results, skipping dummyHeada

# sum % 10: gives the last digit of a number.
# sum // 10: gives how many tens are in the number — i.e. the carry.
