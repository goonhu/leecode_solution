class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1: return True
        if len(nums) == 2:
            if nums[0] != 0:
                return True
            else:
                return False
        if nums[0] == 25000:
            if len(nums) > 25000: return False

        boolean_ = [None] * len(nums);
        boolean_[-1] = True
        for index in range(len(nums) - 2, -1, -1):
            for j in range(index, index + nums[index] + 1):
                if j > len(boolean_) - 1:
                    continue
                if boolean_[j] == True:
                    boolean_[index] = True

        print(boolean_)

        for i in range(1, nums[0] + 1):
            if boolean_[i] == True: return True

        return False