# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        my_q = deque([root])
        while my_q:
            length = len(my_q)
            temp_arr = []
            for i in range(length):
                removed_node = my_q.popleft()
                if removed_node.left:
                    my_q.append(removed_node.left)
                if removed_node.right:
                    my_q.append(removed_node.right)
                temp_arr.append(removed_node.val)

            result.append(temp_arr)

        return result