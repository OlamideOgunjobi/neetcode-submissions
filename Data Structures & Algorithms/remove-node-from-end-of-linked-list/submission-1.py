# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None:
            return None

        front = head
        back = head

        for i in range(n):
            front = front.next
            if (front == None):
                return head.next

        while front.next != None:
            front = front.next
            back = back.next

        back.next = back.next.next

        return head