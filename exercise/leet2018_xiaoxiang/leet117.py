# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        fifo = self.levelTraverse(root)
        for i in range(len(fifo)):
            if i < len(fifo) - 1 and fifo[i][1] == fifo[i + 1][1]:
                fifo[i][0].next = fifo[i + 1][0]

    def levelTraverse(self, root):
        fifo = []
        if root is None:
            return []
        fifo.append((root, 0))
        rd = 0
        res = []
        while rd < len(fifo):
            ptr = fifo[rd][0]
            level = fifo[rd][1]
            if ptr.left is not None:
                fifo.append((ptr.left, level + 1))
            if ptr.right is not None:
                fifo.append((ptr.right, level + 1))
            rd += 1
        return fifo

if __name__ == "__main__":
    s = Solution()
    s.connect()