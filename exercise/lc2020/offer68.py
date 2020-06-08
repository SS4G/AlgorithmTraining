from G55Utils.Py.Utils import TreeNode
class Solution(object):
    def __init__(self):
        self.FIND_P = 1
        self.FIND_Q = 2
        self.FIND_ALL = 3
        self.FIND_NONE = 4
        self.SET_FIND_PQ = set(self.FIND_P, self.FIND_Q)
        

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        commonRootRes = [None,]
        self.checkPQ(root, p, q, commonRootRes)
        return commonRootRes[0]

    def checkPQ(self, root, p, q, commonRootRes):
        if root is None:
            return self.FIND_NONE
        elif root.left is None and root.right is None:
            if root is p:
                return self.FIND_P
            elif root is q:
                return self.FIND_Q
            else:
                return self.FIND_NONE
        else:
            leftRes = self.checkPQ(root.left, p, q, commonRootRes)
            rightRes = self.checkPQ(root.right, p, q, commonRootRes)
            if root is p:
                middleRes = self.FIND_P
            elif root is q:
                middleRes = self.FIND_Q
            else:
                middleRes = self.FIND_NONE

            res = set([leftRes, rightRes, middleRes])

            if  self.FIND_ALL in res:
                return self.FIND_ALL
            elif self.SET_FIND_PQ.issubset(res):
                commonRootRes[0] = root
                return self.FIND_ALL
            elif self.FIND_P in res:
                return self.FIND_P
            elif self.FIND_Q in res:
                return self.FIND_Q
            else:
                return self.FIND_NONE
                

