# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced_bool = True
        def height(self, root):
            nonlocal balanced_bool
            if not root:
                return 0
            
            left = height(self, root.left)
            right = height(self, root.right)

            if not abs(left - right) <= 1:
                balanced_bool = False
            return 1 + max(left, right)


        height(self, root)        
        return balanced_bool

        
        
        
        # if not self.isBalanced(root.left) - self.isBalanced(root.right) <= 1:
        #     return false