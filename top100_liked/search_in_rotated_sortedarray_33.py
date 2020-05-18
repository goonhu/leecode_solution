class Solution:
    def search(self, nums: List[int], target: int) -> int:
        copied = nums.copy()
        nums.sort()
        if target not in nums:
            return -1
        else:
            for index, value in enumerate(copied):
                if value == target: return index
