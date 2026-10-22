# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_node = root 
        # Stack will simulate the "parent pointers" we do NOT have.
        stack = []
        while curr_node or stack:
            #Inorder traversal is:
            # LEFT -> NODE -> RIGHT
            # So before visiting any node,
            # go as far LEFT as possible.
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            # now curr_node is none since we reached left most element 
            # pop from stack this is the smallest element 
            curr_node = stack.pop()
            k -= 1
            if k == 0:
                return curr_node.val
            #After visiting the current node,
            # inorder says we must explore its RIGHT subtree.
            curr_node = curr_node.right
        return -1
