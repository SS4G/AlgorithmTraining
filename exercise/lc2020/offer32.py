
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        rd = 0
        fifo = []
        fifo.append((root, 0))
        while rd < len(fifo):
            leftNode = fifo[rd][0].left
            rightNode = fifo[rd][0].right
            currentLevel = fifo[rd][1]
            if leftNode is not None:
                fifo.append((leftNode, currentLevel + 1))
            if rightNode is not None:
                fifo.append((rightNode, currentLevel + 1))
            rd += 1
        res = []
        for n in fifo:
            if len(res) < n[1] + 1:
                res.append([])
            res[n[1]].append(n[0].val)
        return res