# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # empty tree
        if not root:
            return None

        
        # saving the right subtree
        tmp_right = root.right
        root.right = root.left
        root.left = tmp_right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        