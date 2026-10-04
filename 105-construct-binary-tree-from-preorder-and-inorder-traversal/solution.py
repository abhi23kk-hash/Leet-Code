class Solution:
    def buildTree(self, preorder, inorder):
        index = {value: i for i, value in enumerate(inorder)}
        self.pre = 0

        def helper(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.pre])
            self.pre += 1

            mid = index[root.val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)