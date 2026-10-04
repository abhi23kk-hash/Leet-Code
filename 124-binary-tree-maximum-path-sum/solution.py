class Solution:
    def maxPathSum(self, root):
        self.a = root.val

        def f(n):
            if not n:
                return 0

            l = max(f(n.left), 0)
            r = max(f(n.right), 0)

            self.a = max(self.a, n.val + l + r)

            return n.val + max(l, r)

        f(root)
        return self.a