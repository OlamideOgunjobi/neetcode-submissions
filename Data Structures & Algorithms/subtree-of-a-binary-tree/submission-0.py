# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def decide(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p and not q:
                return False
            if q and not p:
                return False
            if not p and not q:
                return True

            if p.val != q.val:
                return False


            return decide(p.left, q.left) and decide(p.right, q.right)

        if root == None and subRoot != None:
            return False

        if decide(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)