## leetcode 41
[leetcode 41](https://leetcode-cn.com/problems/first-missing-positive/)

## solution
主要使用的是原地hash的方法 基本思路就是 吧 `[1, N]` 的整数放在`[0, N-1]`个地址空间上 `arr[0] = 1 arr[1] = 2 ....` 以此类推
如果某个位置没有对应的整数就标记为None 这样通过查找数组第一个None的位置就知道第一个缺失的整数。

将数组变成上述数组的方式是0开始选定一个位置 将对应位置的数字放到其对应数组的位置 比如当前位置为`arr[0]`的数字是5 那么就将其放到`arr[4]`的位置 将`arr[4]` 原有位置的数字暂存到`arr[0]` 然后循环这一过程. 循环过程中 遇到超出N的数字直接将`arr[0]`记为 `None`然后结束`arr[0]`位置的循环。否则直到 `arr[0] = 1` 或 `arr[0] = None`

### code
```Python
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
```