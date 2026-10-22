# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_node = root 
        stack = []
        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left

            curr_node = stack.pop()
            k -= 1
            if k == 0:
                return curr_node.val
            curr_node = curr_node.right
        return -1
