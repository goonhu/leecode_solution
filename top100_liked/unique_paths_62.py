

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        downs = (n-1); rights = (m-1); alls = downs+rights
        a = math.factorial(alls)
        b = math.factorial(downs)
        c = math.factorial(rights)
        ans = a//(b*c)
        return ans

