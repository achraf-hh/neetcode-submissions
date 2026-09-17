# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        def add(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0

            carry, val = divmod(v1 + v2 + carry, 10)
            next_node = add(
                n1.next if n1 else None,
                n2.next if n2 else None,
                carry

            )
            return ListNode(val, next_node)
        dummy.next = add(l1, l2, 0)
        return dummy.next
            
            