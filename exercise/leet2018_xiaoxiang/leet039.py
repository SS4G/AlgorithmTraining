class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        stack = []
        output = []
        candidates = set(candidates)
        self.combineRecure(candidates, target, -65536, stack, output)
        return output

    def combineRecure(self, candidates, target, limit, stack, output):
        for i in candidates:
            if i >= limit:
                if i == target:
                    stack.append(i)
                    output.append(stack[:])
                    stack.pop()
                elif i > target:
                    continue
                else:
                    stack.append(i)
                    self.combineRecure(candidates, target - i, limit=i, stack=stack, output=output)
                    stack.pop()

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))