# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = 0
        curr = head

        while curr.next != None:
            if i % 2 == 0:
                end = curr
                before_end = end

                while end.next != None:
                    before_end = end
                    end = end.next
                
                
                before_end.next = None
                end.next = curr.next
                curr.next = end
                curr = curr.next
                i += 1
            else:
                curr = curr.next
                i += 1 