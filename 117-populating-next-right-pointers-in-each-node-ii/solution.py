from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = deque([root])

        while q:
            s = len(q)

            for i in range(s):
                n = q.popleft()

                if i < s - 1:
                    n.next = q[0]

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return root