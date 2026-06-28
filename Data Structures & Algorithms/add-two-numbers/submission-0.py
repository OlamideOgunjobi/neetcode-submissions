# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # none empty so no empty condition needed


        carry = 0
        head = None
        curr = head

        l1_val = l1.val
        l2_val = l2.val

        # Edge Case:
        # 1. When the is only one node left
        # 2. When there is no nodes left but there is a carry
        
        while True:
            total_sum = l1_val + l2_val + carry
            
            carry = total_sum // 10                     # Ex: carry = 469 // 10 = 46
            total_sum %= 10                             # Ex: total_sum = 469 % 10 = 9


            # if there is no new list yet
            if not head:
                curr = new_node = ListNode(total_sum)
                head = curr
            else:
                curr.next = new_node = ListNode(total_sum)
                curr = curr.next


            total_sum = 0
            # breaking condition: no need to create a new node
            if (not l1.next) and (not l2.next) and (carry == 0):
                break

            # update the current nodes
            if l1.next:
                l1 = l1.next
                l1_val = l1.val
            else:
                l1_val = 0

            if l2.next:
                l2 = l2.next
                l2_val = l2.val
            else:
                l2_val = 0

            

        return head