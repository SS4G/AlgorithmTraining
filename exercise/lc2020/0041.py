class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        wr = 0
        rd = 0
        cnt = 0
        # 把所有的正整数都压缩在前面
        while rd < len(nums):
            if nums[rd] > 0:
                nums[wr] = nums[rd]
                wr += 1
                cnt+=1
            rd += 1
        N = cnt
        # [1, N] -> [0, N - 1]
        tmp = None
        for idx in range(N):
            while nums[idx] is not None and nums[idx] != idx + 1:
                insertVal = nums[idx]
                if insertVal > N:
                    nums[idx] = None
                    continue
                if nums[insertVal - 1] is not None:
                    if nums[insertVal - 1] != insertVal:
                        tmp = nums[insertVal - 1]
                        nums[insertVal - 1] = insertVal
                        nums[idx] = tmp
                    else:
                        nums[idx] = None
                else:
                    nums[insertVal - 1] = insertVal
                    nums[idx] = None

        for i in range(N):
            if nums[i] is None:
                return i + 1
        return N + 1

if __name__ == "__main__":
    a = [7,8,9,11,12]
    s = Solution()
    assert s.firstMissingPositive([7,8,9,11,12]) == 1
    assert s.firstMissingPositive([1,2,0]) == 3
    assert s.firstMissingPositive([3,4,-1,1]) == 2
    assert s.firstMissingPositive([4, 3, 2, 1]) == 5
    assert s.firstMissingPositive([1, 1]) == 2


              
