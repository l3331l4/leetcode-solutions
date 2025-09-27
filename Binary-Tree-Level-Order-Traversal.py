# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs():
            q = deque()
            q.append(root)
            res = []

            while q:
                qLen = len(q)
                level = []
                for _ in range(qLen):
                    node = q.popleft()

                    if node:
                        q.append(node.left)
                        q.append(node.right)
                        level.append(node.val)

                if level:
                    res.append(level)
            
            return res
        
        return bfs()

                

            