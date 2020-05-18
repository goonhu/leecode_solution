class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        converted = []

        if target not in nums:
            return [-1, -1]
        else:
            for index, value in enumerate(nums):
                if value == target:
                    converted.append((index, value))

        return [converted[0][0], converted[-1][0]]
