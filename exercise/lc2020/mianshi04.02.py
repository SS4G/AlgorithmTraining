# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.genBSTHelper(nums)

    def genBSTHelper(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            middleIdx = len(nums) >> 1
            middleNum = nums[middleIdx]
            middleNode = TreeNode(middleNum)
            middleNode.left = self.genBSTHelper(nums[:middleIdx])
            middleNode.right = self.genBSTHelper(nums[middleIdx + 1:])
            return middleNode
