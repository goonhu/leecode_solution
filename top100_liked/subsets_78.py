
from itertools import chain, combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []; s = nums
        a = chain.from_iterable((combinations(s, r)) for r in range(len(s ) +1))
        for i in a:
            # print(type(i))
            answers.append(list(i))

        return answers

