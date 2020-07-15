## leetcode 204
[leetcode 204](https://leetcode-cn.com/problems/count-primes/)
就是找到所有小于n的质数的个数

### solution
使用了标记法 并且使用列表复制的方式来加速
1. 标记法求质数的方法是 从小到大 如果找到一个质数x 那么 所有的 n*x 必然都是非质数 所以全部标记为合数
2. 在标记范围的选择上，假设x 是质数 那么 只标记 比 大于等于`x * x`的合数 因为 `(x - 1) * x` 这个合数 如果`(x-1)`是质数 那么 `(x - 1) * x`已经在之前被标记过了， 如果`(x - 1)`是合数， 那么`(x - 1) * x`至少在之前访问`(x - 1)`的某个质因数的时候标记过了。
3. 因为在2中说了 只标记 大于等于`x * x`的合数 所以 只要检索质数到`sqrt(x)`(含) 之前就可以可 所以这样的复杂度只有 `O(m * sqrt(x))`

### code
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