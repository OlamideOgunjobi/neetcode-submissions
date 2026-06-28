# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # concept: traverse the two lists and insert sorting into a new linked lists
        # both lists are sorted
        # check if one list is empty, if it is retun the other, if both are empty return None
        # if both are not none, create an empty list to store the new merged list
        # while you haven't reached the end of both, traverse both at the same time
        # if list1's value is less than list2's, append that to the new list, move list1 and the new lists curr pointer forward
        # follow similar step for list2 is list2's value is less
        # if 

        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return None

        head = None
        curr = None

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        elif list2.val < list1.val:
            head = list2
            list2 = list2.next

        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            elif list2.val < list1.val:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if list1 and not list2:
            curr.next = list1
        elif list2 and not list1:
            curr.next = list2

        return head