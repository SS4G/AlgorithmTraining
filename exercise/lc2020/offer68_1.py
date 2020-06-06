#from G55Utils.Py.Utils import TreeNode
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        pval = p.val if p.val < q.val else q.val
        qval = q.val if q.val >= q.val else p.val
        res = [None,]
        self.traverseHelper(root, pval, qval, res)
        return res[0]
    
    def traverseHelper(self, root, pval, qval, res):
        if root is None:
            return False
        elif res[0] is not None:
            return True
        elif pval <= root.val <= qval:
            res[0] = root
            return True
        elif root.val > qval:
            return self.traverseHelper(root.left, pval, qval, res)
        else:
            return self.traverseHelper(root.right, pval, qval, res)
            
if __name__ == "__main__":
    root = TreeNode(2)
    left = TreeNode(1)
    s = Solution()
    res = s.lowestCommonAncestor(root, left, root)
    print(res.val)