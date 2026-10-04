from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        q = deque([root])
        a = []

        while q:
            t = []

            for _ in range(len(q)):
                n = q.popleft()
                t.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            a.append(t)

        return a[::-1]