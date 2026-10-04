class Solution:
    def pathSum(self, root, s):
        a = []

        def f(n, t, p):
            if not n:
                return

            p.append(n.val)
            t += n.val

            if not n.left and not n.right:
                if t == s:
                    a.append(p[:])
            else:
                f(n.left, t, p)
                f(n.right, t, p)

            p.pop()

        f(root, 0, [])
        return a