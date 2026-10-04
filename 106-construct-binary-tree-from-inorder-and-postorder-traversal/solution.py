class Solution:
    def buildTree(self, inorder, postorder):
        d = {v: i for i, v in enumerate(inorder)}
        self.i = len(postorder) - 1

        def f(l, r):
            if l > r:
                return None

            n = TreeNode(postorder[self.i])
            self.i -= 1

            m = d[n.val]

            n.right = f(m + 1, r)
            n.left = f(l, m - 1)

            return n

        return f(0, len(inorder) - 1)