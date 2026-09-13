# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next: return
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
        head = head
        second = reverse(second)
        dummy = ListNode(None)
        curr = dummy
        while head and second:
            temp = head.next
            curr.next = head
            curr.next.next = second
            curr = curr.next.next
            head = temp
            second = second.next
        if not head:
            curr.next = second
        if not second:
            curr.next = head


