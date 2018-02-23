class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        record = {0: 0}
        coins.sort()
        res = self.minCoin(coins, amount, record)
        return -1 if res == 6553600 else res

    def minCoin(self, coins, amount, record):
        if amount in record:
            return record[amount]
        #print(amount)
        #input("")
        if amount == 0:
            return 0
        elif amount < 0:
            return 6553600
        else:
            minCoins = 6553600
            for c in coins:
                #print("c", c)
                if amount - c < 0:
                    return 6553600
                minCoins = min(1 + self.minCoin(coins, amount - c, record), minCoins)
            record[amount] = minCoins
            return minCoins

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 100))
    print(s.coinChange([370, 417, 408, 156, 143, 434, 168, 83, 177, 280, 117], 9953))
    9953