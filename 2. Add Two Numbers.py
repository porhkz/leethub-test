# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode(0)
        curr = l3

        while l1 != None or l2 != None or carry != 0:
            val1 = 0
            val2 = 0

            if l1 != None:
                val1 = l1.val
                l1 = l1.next              
            
            if l2 != None:
                val2 = l2.val
                l2 = l2.next

            val_sum = val1 + val2 + carry

            carry, result = divmod(val_sum, 10)

            curr.next = ListNode(result)
            curr = curr.next

        return l3.next


            