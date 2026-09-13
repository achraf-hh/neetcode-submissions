# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            curr = node
            prev, temp = None, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        first = head
        second = reverse(second)
        dummy = ListNode(None)
        curr = dummy
        while first and second:
            temp = first.next
            curr.next = first
            curr.next.next = second
            curr = curr.next.next
            first = temp
            second = second.next
        if not first:
            curr.next = second
        if not second:
            curr.next = first


