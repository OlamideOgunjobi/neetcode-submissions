# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if both are empty:
        if list1 and list2 == None:
            return list1
        elif list1 == None and list2:
            return list2
        elif not list1 and not list2:
            return None

        head = None
        curr = None


        # while both are not empty
        while list1 and list2:

            if list1.val <= list2.val:
                if not head:    # just starting the output list
                    head = list1
                    curr = head
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next

            elif list1.val > list2.val:
                if not head:    # just starting the output list
                    head = list2
                    curr = head
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
                
            
                
        if list1 and not list2:
            curr.next = list1
        elif not list1 and list2:
            curr.next = list2



        return head