# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        while node:
            # if the both targets are greater than node value move RIGHT
            if p.val > node.val and q.val > node.val:
                node = node.right

            # if the both target are lesser than node Value then move LEFT
            elif p.val < node.val and q.val < node.val:
                node = node.left
            
            # if they split apart, that is, if left is greater/lesser and right greater/lesser to node 
            else:
                return node

        return None
            