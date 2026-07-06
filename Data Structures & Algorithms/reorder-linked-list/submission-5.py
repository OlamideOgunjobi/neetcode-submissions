# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return None
        elif not head.next:
            return None


        # STEP 1: FIND THE MIDDLE
        slow = head
        fast = head

        # at the end of the loop, slow would be in the middle
        while fast and fast.next:
            chop = slow
            slow = slow.next
            fast = fast.next.next

        chop.next = None

        # STEP 2: REVERSE THE SECOND HALF

        curr = slow
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev is now the start of the second half

        # Merge the two




        final = head
        it = head
        head = head.next
        print(f"it: {it.val}")
        while head and prev:
            it.next = prev
            prev = prev.next
            it = it.next
            print(f"it: {it.val}")
            it.next = head
            head = head.next
            it = it.next
            print(f"it: {it.val}")
            
            
        if prev:
            it.next = prev

        return None

        
