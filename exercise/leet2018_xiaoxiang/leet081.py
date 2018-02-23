class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        st = 0
        ed = len(nums) - 1
        if len(nums) < 1:
            return False

        if nums[0] == nums[-1] and nums[0] == target:
            return True
        elif nums[0] == nums[-1]:
            while st < ed and nums[st] == nums[ed]:
                if nums[st] == target:
                    return True
                st += 1
                ed -= 1

            if st <= ed:
                return self.search0(nums, target, st, ed + 1) != -1
            else:
                return False
        else:
            # print("22")
            return self.search0(nums, target, st, ed + 1) != -1

    def search0(self, nums, target, st, ed):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[st] <= nums[ed - 1]:
            # print("ssss")
            return self.generalBinSearch(nums, st, ed, target)
        else:
            avr = nums[ed - 1]
            lowestIdx = self.findPulse(nums, st, ed, avr)
            if target > avr:
                return self.generalBinSearch(nums, st, lowestIdx, target)
            else:
                return self.generalBinSearch(nums, lowestIdx, ed, target)

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
            # print(lo, hi, mid)
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
            # print(lo, hi, mid)
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
    nums = [3, 4, 5, 1, 2]
    assert s.search(nums, 4)
    assert not s.search(nums, 6)
    nums = [3, 3, 3, 4, 4, 4, 5, 5, 5, 1, 2, 3, 3, 3]
    assert s.search(nums, 5)
    assert not s.search(nums, 6)
    nums = [1, 2, 1]
    assert s.search(nums, 2)