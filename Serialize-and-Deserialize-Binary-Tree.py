# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                res += "%"
                stringval = str(node.val)
                res += stringval
            else:
                res += "%"
                res += "*"

            if node:
                q.append(node.left)
                q.append(node.right)

        print(res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i = 0
        n = len(data)
        curr = ""

        q = deque()

        while i < n:
            c = data[i]
            if c == "%":
                if curr:
                    val = int(curr)
                    q.append(val)
                if data[i+1] == "*":
                    q.append(None)
                    curr = ""
                    i += 1
                curr = ""
            else:
                curr += c
            i += 1

        val = q.popleft()
        if val is None:
            return []
            
        root = TreeNode(val)
        parentq = deque([root])

        while q:
            node = parentq.popleft()

            leftval = q.popleft()

            if leftval is not None:
                node.left = TreeNode(leftval)
                parentq.append(node.left)

            rightval = q.popleft()
            if rightval is not None:
                node.right = TreeNode(rightval)
                parentq.append(node.right)

        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))