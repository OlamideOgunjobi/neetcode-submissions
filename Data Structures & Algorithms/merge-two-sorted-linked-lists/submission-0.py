# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # given lists are already sorted

        # dealing with any empty lists
        if list1 == None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2


        mergedList = None
        currNode = None

        # case where both lists are not empty
        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                if mergedList == None:
                    mergedList = list1
                    currNode = mergedList
                else:
                    currNode.next = list1
                    currNode = currNode.next
                list1 = list1.next
                

            elif list2.val < list1.val:
                if mergedList == None:
                    mergedList = list2
                    currNode = mergedList
                else:
                    currNode.next = list2
                    currNode = currNode.next

                list2 = list2.next
            


        # the case where one of them is not empty yet
        if list1 != None:
            currNode.next = list1
        elif list2 != None:
            currNode.next = list2

        return mergedList