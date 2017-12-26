# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from AlgorithmTraining.G55Utils.Py.Utils import *

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        markDict = {}
        self.markLeaf(root, markDict, k)
        items = list(markDict.items())
        items.sort(key=lambda item: item[1])
        return items[0].val

    def markLeaf(self, root, markDict, target):
        pathStack = []
        output = []
        self.traverse(root, pathStack, target, output)
        traversed = set([])
        pathStack = output
        pathStack.reverse()
        for i in range(len(pathStack)):
            markDict[pathStack[i]] = i
        for node in markDict:
            self.markDownLeaf(node, traversed, markDict, markDict[node])

    def traverse(self, root, pathStack, target, output):
        if root is None:
            return
        pathStack.append(root)
        if root.val != target:
            self.traverse(root.left, pathStack, target, output)
            self.traverse(root.right, pathStack, target, output)
        else:
            output.append(pathStack[:])
        pathStack.pop()

    def markDownLeaf(self, root, traversed, distDict, lastDist):
        if root is None:
            return
        if root in traversed:  # checked
            return
        traversed.add(root)
        if root.left is None and root.right is None:  # is leaf
            distDict[root] = lastDist + 1
        else:
            self.markDownLeaf(root.left, traversed, distDict, lastDist + 1)
            self.markDownLeaf(root.right, traversed, distDict, lastDist + 1)

if __name__ == "__main__":
    s = Solution()
    root = TreeUtil.deserialize([1, 2, 3, 4, None, None, None, 5, None, 6])
    print("Nearest", s.findClosestLeaf(root, 2))