class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        save_dic = {}
        for i in range(len(nums)):
            save_dic[i] = None

        save_dic[0] = nums[0]
        for index in range(1, len(nums)):
            save_dic[index] = max((save_dic[index - 1] + nums[index]), nums[index])

        return max(save_dic.values())

