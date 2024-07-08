from functools import lru_cache

class Solution:
    dict_of_res = {}
    @lru_cache(maxsize=1000)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1 or n == 2:
            return 1 
        if n > 2:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

obj1 = Solution()

print(obj1.tribonacci(31))        