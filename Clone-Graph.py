"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        q = deque()
        q.append(node)

        old_to_new = {}
        copy = Node(node.val)
        old_to_new[node] = copy

        while q:
            curr = q.popleft()

            for neigh in curr.neighbors:
                if neigh not in old_to_new:

                    old_to_new[neigh] = Node(neigh.val)
                    q.append(neigh)

                old_to_new[curr].neighbors.append(old_to_new[neigh])

        return old_to_new[node]

        