class Solution:
    def flatten(self, root):
        self.p = None

        def f(n):
            if not n:
                return

            f(n.right)
            f(n.left)

            n.right = self.p
            n.left = None
            self.p = n

        f(root)