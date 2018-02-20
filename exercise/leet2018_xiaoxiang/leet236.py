from AlgorithmTraining.G55Utils.Py.Utils import *

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = []
        path = {}
        self.traverseRecure(root, stack, path, p, q)
        pPath = path["p"]
        qPath = path["q"]
        i = 0
        lastAncestor = None
        while i < min(len(pPath), len(qPath)) and pPath[i] is qPath[i]:
            lastAncestor = pPath[i]
            i += 1
        return lastAncestor

    def traverseRecure(self, root, stack, path, p, q):
        if root is not None:
            stack.append(root)
            if root is p:
                path["p"] = stack[:]
            if root is q:
                path["q"] = stack[:]
            self.traverseRecure(root.left, stack, path, p, q)
            self.traverseRecure(root.right, stack, path, p, q)
            stack.pop()

if __name__ == "__main__":
    s = Solution()
    root = TreeUtil.deserialize([3, 5, 1, 6, 2, 0, 8, None, 7, 4])
    p = root.left
    q = root.right
    print(s.lowestCommonAncestor(root, p, q).val)