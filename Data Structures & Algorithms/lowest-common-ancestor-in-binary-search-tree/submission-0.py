# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr_node = root 
        while curr_node:
            if p.val < curr_node.val and q.val < curr_node.val:
                curr_node = curr_node.left
            elif p.val > curr_node.val and q.val > curr_node.val:
                curr_node = curr_node.right
            else:
                return curr_node
        return null

