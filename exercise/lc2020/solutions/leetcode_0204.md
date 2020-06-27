### tips
使用了标记法 并且使用列表复制的方式来加速
```Python
class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        num_list = [True]*n
        num_list[0], num_list[1] = False, False

        for i in range(2, int(pow(n, 0.5)) + 1):
            if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
                num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

        return sum(num_list) 
```