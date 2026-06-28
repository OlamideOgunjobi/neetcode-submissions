# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # empty list case
        if head == None:
            return

        prevNode = None
        currNode = head
        nextNode = None
        # when the list is not empty
        while currNode != None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        head = prevNode
        return head
