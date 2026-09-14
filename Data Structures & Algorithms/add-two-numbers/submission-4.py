# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        def reverse(curr):
            prev, temp = None, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        if l1.val == 0:
            return reverse(l2)
        if l2.val == 0:
            return reverse(l1)
        if l2.val == l1.val == 0:
            return ListNode(0)
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        res = num1 + num2
        dummy = ListNode(None)
        curr = dummy
        while res > 0:
            r = res % 10
            node = ListNode(val = r)
            curr.next = node
            curr = node
            res = res//10
        return dummy.next
        