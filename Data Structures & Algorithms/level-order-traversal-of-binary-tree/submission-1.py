# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

        q = deque()
        result = []

        if root:
            q.append(root)

        while q:

            q_len = len(q)
            sub_arr = []

            i = 0
            while i < q_len:
                curr = q.popleft()
                sub_arr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                i += 1

            result.append(sub_arr)

        return result
            
        