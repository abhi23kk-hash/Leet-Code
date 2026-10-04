class Solution:
    def connect(self, root):
        if not root:
            return None

        q = [root]

        while q:
            t = []

            for i in range(len(q)):
                if i < len(q) - 1:
                    q[i].next = q[i + 1]

                if q[i].left:
                    t.append(q[i].left)
                if q[i].right:
                    t.append(q[i].right)

            q = t

        return root