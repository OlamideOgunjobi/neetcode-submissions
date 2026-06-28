# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # keep track of the previous, current, and next pointers
        # While curr the current node is not null
        # On each iteration
            # update the next pointer
            # update the curr.next pointer
            # update curr
            # then update prev
        # return previous because curr would be null since the while loop ended

        prev = None
        curr = head
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev