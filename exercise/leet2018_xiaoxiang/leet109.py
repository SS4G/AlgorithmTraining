from AlgorithmTraining.G55Utils.Py.Utils import *

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        li = []
        while head is not None:
            li.append(head.val)
            head = head.next
        return self.toBST(li)

    def toBST(self, li):
        if len(li) == 0:
            return None
        idx = len(li) >> 1
        root = TreeNode(li[idx])
        root.left = self.toBST(li[:idx])
        root.right = self.toBST(li[idx + 1:])
        return root