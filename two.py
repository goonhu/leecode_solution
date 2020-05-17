class Solution:

    def twoSum(self, nums, target):
        hash_ = {}
        for index, element in enumerate(nums):
            n = target - element
            if n not in hash_:
                hash_[element] = index
            else:
                return [hash_[n], index]




