class Solution:
    def hasPathSum(self, root, s):
        if not root:
            return False

        if not root.left and not root.right:
            return s == root.val

        s -= root.val

        return self.hasPathSum(root.left, s) or self.hasPathSum(root.right, s)