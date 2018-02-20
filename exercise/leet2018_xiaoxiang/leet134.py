class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        earn = [None for i in range(len(gas))]
        for i in range(len(gas)):
            earn[i] = gas[i] - cost[i]
        i = 0
        curGas = 0
        st = i
        #print(earn)
        while True:
            curGas += earn[i]
            #print("c", curGas)
            if curGas < 0:
                oldst = st
                st = i + 1 if i + 1 < len(earn) else 0
                if st <= oldst:
                    return -1
                else:
                    curGas = 0
            else:
                if (i + 1 if i + 1 < len(earn) else 0) == st:
                    return st
            i = i + 1 if i + 1 < len(earn) else 0
        return -1

if __name__ == "__main__":
    s = Solution()
    gas = [1,2,3,3]
    cost = [2,1,5,1]
    print(s.canCompleteCircuit(gas, cost))