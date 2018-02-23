class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        if nums[0] <= nums[-1]:
            return self.generalBinSearch(nums, 0, len(nums), target)
        else:
            avr = nums[-1]
            lowestIdx = self.findPulse(nums, 0, len(nums), avr)
            if target > avr:
                return self.generalBinSearch(nums, 0, lowestIdx, target)
            else:
                return self.generalBinSearch(nums, lowestIdx, len(nums), target)

    def findPulse(self, arr, st, ed, avr):
        """
        :param arr:
        :param st:
        :param ed:
        :param avr:
        :return: idx of lowest point
        """
        lo = st
        hi = ed - 1
        mid = (lo + hi) >> 1
        while lo <= hi:
            print(lo, hi, mid)
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return mid
            elif arr[mid] <= avr:
                hi = mid - 1
            elif arr[mid] > avr:
                lo = mid + 1
            mid = (lo + hi) >> 1
        return -1

    def generalBinSearch(self, arr, st, ed, target):
        lo = st
        hi = ed - 1
        mid = (lo + hi) >> 1
        while lo <= hi:
            #print(lo, hi, mid)
            if arr[mid] < target:
                lo = mid + 1
            elif arr[mid] > target:
                hi = mid - 1
            else:
                return mid
            mid = (lo + hi) >> 1
        return -1

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    print(s.generalBinSearch(nums, 0, 5, 3))
    nums = [1, 2, 3, 4]
    print(s.generalBinSearch(nums, 0, 4, 3))
    nums = [1, 2]
    print(s.generalBinSearch(nums, 0, 2, 2))
    pulse = [4, 5, 6, 7, 8, 1, 2, 3]
    print(s.findPulse(pulse, 0, 8, 3))
    print(s.search(pulse, 7))
