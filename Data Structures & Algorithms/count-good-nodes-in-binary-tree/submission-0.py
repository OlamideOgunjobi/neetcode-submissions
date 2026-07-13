# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def trav(root, maxval):
            if not root:
                return 0

            if root.val >= maxval:
                maxval = root.val
                return 1 + trav(root.left, maxval) + trav(root.right, maxval)
            else:
                return 0 + trav(root.left, maxval) + trav(root.right, maxval)

        return trav(root, root.val)