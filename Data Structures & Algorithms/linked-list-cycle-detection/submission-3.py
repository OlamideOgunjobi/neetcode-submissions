# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # use Floyd's Cycle-Finding Algorithm
        # use Fast and Slow pointer to traverse the list
        # fast increments by 2 while slow by 1
        # if the two equal each other, there is a cycle
        # however, if the fast eqauls null, no cycle (no need to check for slow since fast would reach end first)

        fast = head
        slow = head

        while fast:

            for i in range(2):
                fast = fast.next
                if fast == None:
                    return False
                
            slow = slow.next

            if fast == slow:
                return True

        return False