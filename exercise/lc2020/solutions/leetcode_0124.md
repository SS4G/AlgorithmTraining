## Leetcod 124


DFS 方法 
1. 一条最大和路径 左边 
### codes 
```Python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxResArray = [0, ]
        maxNegValueArray = [-0xfffffffff]

        maxPathRootValue = self.maxValueHelper(root, maxResArray, maxNegValueArray)
        if maxNegValueArray[0] >= 0:
            return maxResArray[0]
        else:
            return maxNegValueArray[0]

    def maxValueHelper(self, root, maxResArray, maxNegValueArray):
        if root is None:
            return 0

        if root.val < 0:
            maxNegValueArray[0] = max(maxNegValueArray[0], root.val)
        elif root.val >= 0:
            maxNegValueArray[0] = 0

        leftMaxSumedValue = self.maxValueHelper(root.left, maxResArray)
        rightMaxSumedValue = self.maxValueHelper(root.right, maxResArray)
        maxPathValue = leftMaxSumedValue + rightMaxSumedValue + root.val
        maxResArray[0] = max(maxResArray[0], maxPathValue)
        rootMaxSumedValue = max(leftMaxSumedValue, rightMaxSumedValue) + root.val
        return max(rootMaxSumedValue, 0)
```