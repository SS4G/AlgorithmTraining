class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minres = 0
        minDist = 0xfffffffff
        for idx in range(len(nums) - 2):
            firstVal = nums[idx]
            restValue = target - firstVal
            leftIndex = idx + 1
            rightIndex = len(nums) - 1
            #print("idx0={}".format(idx))
            while leftIndex < rightIndex:
                #print("left={} right={}".format(leftIndex, rightIndex))
                currentDist = restValue - (nums[leftIndex] + nums[rightIndex])
                if currentDist > 0:
                    #print("left={} right={}".format(leftIndex, rightIndex))
                    if abs(currentDist) < minDist:
                        minres = nums[leftIndex] + nums[rightIndex] + firstVal
                        minDist = abs(currentDist)
                    leftIndex += 1
                elif currentDist < 0:
                    #print("left={} right={}".format(leftIndex, rightIndex))
                    if abs(currentDist) < minDist:
                        minres = nums[leftIndex] + nums[rightIndex] + firstVal
                        minDist = abs(currentDist)
                    rightIndex -= 1
                else:
                    return target
        return minres

if __name__ == "__main__":
    s = Solution()
    arr = [-1,2,1,-4]
    target = 1
    print(s.threeSumClosest(arr, target))
