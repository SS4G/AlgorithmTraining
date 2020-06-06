from G55Utils.Py.Utils import TreeNode
class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        traverseList = []
        result = [None,]
        self.traverseHelper(root, traverseList, k, result)
        return result[0]

    def traverseHelper(self, root, traverseList, k, result):
        if root is None:
            return True
        res = self.traverseHelper(root.right, traverseList, k, result)
        if not res:
            return res
        traverseList.append(root.val)
        if len(traverseList) == k:
            result[0] = root.val
            return False
        res = self.traverseHelper(root.left, traverseList, k, result)
        if not res:
            return res
        return True
