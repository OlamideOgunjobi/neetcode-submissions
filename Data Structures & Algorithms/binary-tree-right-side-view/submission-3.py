# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        from collections import deque

        result = []

        q = deque()

        if root:
            q.append(root)

        while q:

            q_len = len(q)
            i = 0

            for i in range(q_len):

                curr = q.popleft()

                if i == q_len - 1:
                    result.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return result

            