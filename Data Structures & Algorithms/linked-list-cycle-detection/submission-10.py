# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        fast = head
        slow = head

        while fast:
            
            for i in range(2):
                if not fast: return False
                fast = fast.next

            slow = slow.next

            if fast == slow:
                return True

        return False