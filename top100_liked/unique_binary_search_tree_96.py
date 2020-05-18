
class Solution:
    def numTrees(self, n: int) -> int:
        trees = [0] * ( n +1)

        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2

        trees[0] = 1; trees[1] = 1; trees[2] = 2



        for i in range(3, n+ 1):
            for j in range(0, i):
                trees[i] += trees[j] * trees[i - 1 - j]

        return trees[n]