

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                nums.insert(nums.pop(i), 0)
                i += 1
            elif nums[i] == 2:
                nums.append(nums.pop(i))
            else:
                i += 1
            print("i :", i)
            print("nums :", nums)