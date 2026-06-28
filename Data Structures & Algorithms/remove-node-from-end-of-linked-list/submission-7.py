# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # check n = 1, if it is just move the tail
        # if not, use curr and prev ptr
        # iterate till at the nth node
        # then remove the node from the list
        # return head
        # NOTE: python automatically deals with garbage collection


        if head == None:
            return None
        

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
            
        if n == length:
            tmp = head
            head = head.next
            tmp.next = None
            return head

        curr = head
        while length > n+1:
            curr = curr.next
            length -= 1

        del_node = curr.next
        curr.next = del_node.next
        del_node.next = None

        print(length)
        return head




