# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def orderTraversal(node):
            nonlocal res
            if not node:
                return 0
            orderTraversal(node.left)
            res.append(node.val)
            orderTraversal(node.right)

        orderTraversal(root)
        return res[k-1]
