class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(k + 1):
            a = i
            b = k - i
            if a > len(nums1) or b > len(nums2):
                continue
            l1 = self.getMaxKnum(nums1, a)
            l2 = self.getMaxKnum(nums2, b)
            #print(l1, l2)
            res.append(tuple(self.merge2(l1, l2)))
        res.sort(reverse=True)
        return list(res[0])

    def getMaxKnum(self, arr, k):
        stack = []
        rundentNum = len(arr) - k
        ptr = 0

        while ptr < len(arr):
            #print("s", stack, arr[ptr])  # ??
            while len(stack) > 0 and rundentNum > 0 and stack[-1] < arr[ptr]:
                stack.pop()
                rundentNum -= 1
            if len(stack) < k:
                stack.append(arr[ptr])
            else:
                rundentNum -= 1
            ptr += 1
        return stack

    def merge2(self, l1, l2):
        ptr1 = 0
        ptr2 = 0
        res = []
        while ptr1 < len(l1) and ptr2 < len(l2):
            print(l1[ptr1], l2[ptr2], ptr1, ptr2)
            if l1[ptr1] == l2[ptr2]:
                cmpRes = self.greaterNum(l1, ptr1, l2, ptr2)
                if cmpRes > 0:
                    res.append(l1[ptr1])
                    ptr1 += 1
                else:
                    res.append(l2[ptr2])
                    ptr2 += 1
            elif l1[ptr1] > l2[ptr2]:
                res.append(l1[ptr1])
                ptr1 += 1
            else:
                res.append(l2[ptr2])
                ptr2 += 1
        while ptr1 < len(l1):
            res.append(l1[ptr1])
            ptr1 += 1
        while ptr2 < len(l2):
            res.append(l2[ptr2])
            ptr2 += 1
        return res

    def greaterNum(self, arr1, nst1, arr2, nst2):
        ptr1 = nst1
        ptr2 = nst2
        assert arr1[nst1] == arr2[nst2], "wtf?"
        t1 = tuple(arr1[nst1:])
        t2 = tuple(arr2[nst2:])
        if t1 > t2:
            return 1
        elif t1 == t2:
            return 0
        else:
            return -1
        #stVal = arr1[nst1]
        #while ptr1 < len(arr1) and arr1[ptr1] == stVal:
        #    ptr1 += 1
        #while ptr2 < len(arr2) and arr2[ptr2] == stVal:
        #    ptr2 += 1
        #
        #if ptr1 == len(arr1) and ptr2 == len(arr2):
        #    return 0
        #elif ptr1 == len(arr1):
        #    return self.cmp(stVal, arr2[ptr2])
        #elif ptr2 == len(arr2):
        #    return self.cmp(arr1[ptr1], stVal)
        #elif ptr1 - nst1 == ptr2 - nst2:
        #    return self.cmp(arr1[ptr1], arr2[ptr2])
        #elif ptr1 - nst1 < ptr2 - nst2:
        #    return self.cmp(arr1[ptr1], stVal)
        #elif ptr1 - nst1 > ptr2 - nst2:
        #    return self.cmp(stVal, arr2[ptr2])
        #else:
        #    return 0

    def cmp(self, a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

if __name__ == "__main__":
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    nums1 = [7, 6, 1, 9, 3, 2, 3, 1, 1]
    nums2 = [4, 0, 9, 9, 0, 5, 5, 4, 7]
    k = 9

    nums1 = [2, 1, 7, 8, 0, 1, 7, 3, 5, 8, 9, 0, 0, 7, 0, 2, 2, 7, 3, 5, 5]
    nums2 = [2, 6, 2, 0, 1, 0, 5, 4, 5, 5, 3, 3, 3, 4]
    k = 35


    s = Solution()
    #print(s.getMaxKnum(nums2, 4))
    print(s.greaterNum(nums1, 4, nums2, 3))
    print(s.maxNumber(nums1, nums2, k))