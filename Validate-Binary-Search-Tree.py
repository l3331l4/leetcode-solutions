# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValidBst(node, minAllowed, maxAllowed):
            if node is None:
                return True

            leftNode = node.left
            rightNode = node.right

            if (leftNode and leftNode.val >= node.val) or (rightNode and rightNode.val <= node.val):
                return False
            
            if (leftNode and leftNode.val <= minAllowed) or (rightNode and rightNode.val >= maxAllowed):
                return False
            
            return checkValidBst(leftNode, minAllowed, node.val) and checkValidBst(rightNode, node.val, maxAllowed)
        
        return checkValidBst(root, -float("inf"), float("inf"))