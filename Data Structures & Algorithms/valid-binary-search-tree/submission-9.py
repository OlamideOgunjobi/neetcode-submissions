# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def check_range(root, left_bound, right_bound):
            # if a nullptr
            if not root:
                return True
            
            if left_bound >= root.val or right_bound <= root.val:
                return False
            else:
                return check_range(root.left, left_bound, root.val) and check_range(root.right, root.val, right_bound)

        return check_range(root, float("-inf"), float("inf"))

