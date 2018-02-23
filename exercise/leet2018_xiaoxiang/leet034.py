class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftBound = self.searchLeft(nums, 0, len(nums), target)
        rightBound = self.searchRight(nums, 0, len(nums), target)
        return [leftBound, rightBound]

    def searchLeft(self, arr, st, ed, target):
        lo = st
        hi = ed - 1
        mid = (lo + hi) >> 1
        while lo <= hi:
            if arr[mid] < target:
                lo = mid + 1
            elif arr[mid] > target or (mid > 0 and arr[mid] == target and arr[mid - 1] == target):
                hi = mid - 1
            else:
                return mid
            mid = (lo + hi) >> 1
        return -1

    def searchRight(self, arr, st, ed, target):
        lo = st
        hi = ed - 1
        mid = (lo + hi) >> 1
        while lo <= hi:
            if arr[mid] < target or (mid < ed - 1 and arr[mid] == target and arr[mid + 1] == target):
                lo = mid + 1
            elif arr[mid] > target:
                hi = mid - 1
            else:
                return mid
            mid = (lo + hi) >> 1
        return -1

if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print(s.searchRange(nums, 8))