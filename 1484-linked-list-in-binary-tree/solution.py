class Solution:
    def isSubPath(self, head, root):
        if not root:
            return False

        def dfs(node, cur):
            if not cur:
                return True
            if not node or node.val != cur.val:
                return False

            return dfs(node.left, cur.next) or dfs(node.right, cur.next)

        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)