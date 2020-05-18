
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        nums = list(set(nums))
        a = sorted(nums)
        print(a); c_max = 1; save_list = [0] * len(nums)
        save_list[0] = 1

        for index in range(0, len(nums)):
            if index != 0:
                if a[index] == a[inde x -1] + 1:
                    save_list[index] = c_ma x +1
                    c_max = c_max + 1
                else:
                    c_max = 1; save_list[index] = c_max
            else: continue

        return max(save_list)

