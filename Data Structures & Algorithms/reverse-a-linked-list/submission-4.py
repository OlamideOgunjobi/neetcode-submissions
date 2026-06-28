# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # need to keep track of curr and prev

        # empty list
        if (not head):
            return None

        prev = None
        curr = head
        nxt = None
            
        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev

        return head

