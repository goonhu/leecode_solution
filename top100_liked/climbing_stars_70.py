class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        dic[1] = 1;
        dic[2] = 2
        if n >= 3:
            for i in range(3, n + 1):
                dic[i] = dic[i - 1] + dic[i - 2]

        return dic[n]