from AlgorithmTraining.G55Utils.Py.Utils import *

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        fifo = []
        if root is None:
            return []
        fifo.append((root, 0))
        rd = 0
        ptr = root
        level = 0
        lastLevel = -1
        res = []
        while rd < len(fifo):
            ptr = fifo[rd][0]
            level = fifo[rd][1]
            if level != lastLevel and rd > 0:
                res.append(fifo[rd - 1][0].val)
            lastLevel = level
            if ptr.left is not None:
                fifo.append((ptr.left, level + 1))
            if ptr.right is not None:
                fifo.append((ptr.right, level + 1))
            rd += 1
        res.append(fifo[-1][0].val)
        return res

if __name__ == "__main__":
    s = Solution()
    root = TreeUtil.deserialize([1, 2, 3, None, 5, None, 4])
    print(s.rightSideView(root))