# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer approach
        
        fast = head
        slow = head
        i = 0

        while fast != None:
            fast = fast.next

            if i == 2:
                slow = slow.next
                i = 0
            else:
                i += 1
            
            if fast == slow:
                return True

        return False