class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c_list = list(set(nums))
        dic = {i: 0 for i in c_list}

        for each in nums:
            dic[each] += 1

        for i, j in dic.items():
            if j == 1: return i

