from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = []
        permutation = permutations(nums, len(nums))

        for each in permutation:
            answers.append(list(each))

        return answers