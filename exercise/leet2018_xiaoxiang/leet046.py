class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        marked = {k: False for k in nums}
        stack = []
        output = []
        self.premuteRecure(nums, marked, stack=stack, output=output)
        return output

    def premuteRecure(self, numbers, marked, stack, output):
        for i in numbers:
            if marked[i] is False:
                marked[i] = True
                stack.append(i)
                if len(stack) < len(numbers):
                    self.premuteRecure(numbers, marked, stack, output)
                else:
                    output.append(stack[:])
                stack.pop()
                marked[i] = False

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    for i in s.permute(nums):
        print(i)