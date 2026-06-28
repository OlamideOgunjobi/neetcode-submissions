# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        # traverse while both lists are not None, calculate and keep trac of carry val

        carry_val = 0
        result = ListNode()
        curr = result

        while l1 and l2:
            answer = l1.val + l2.val + carry_val
            carry_val = 0
            if answer > 9:
                answer -= 10
                carry_val += 1

            curr.val = answer
            if l1.next or l2.next:
                curr.next = ListNode()
                curr = curr.next

            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                answer = l1.val + carry_val
                carry_val = 0
                if answer > 9:
                    answer -= 10
                    carry_val += 1
                curr.val = answer
                if l1.next:
                    curr.next = ListNode()
                    curr = curr.next
                l1 = l1.next
        elif l2:
            while l2:
                answer = l2.val + carry_val
                carry_val = 0
                if answer > 9:
                    answer -= 10
                    carry_val += 1
                curr.val = answer
                if l2.next:
                    curr.next = ListNode()
                    curr = curr.next
                l2 = l2.next

        if carry_val != 0:
            curr.next = ListNode()
            curr = curr.next
            curr.val = carry_val

        return result
            