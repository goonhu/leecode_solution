class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new_ = []
        for element in nums:
            if element >= 0: new_.append(element)

        if len(new_) == 0: return 1
        new_.sort()
        min_ = new_[0];
        max_ = new_[-1]
        if min_ <= 1:
            for i in range(min_, max_ + 1):
                if i not in new_:
                    if i > 0:
                        return i
                    else:
                        continue

            if (max_ + 1) > 0:
                return max_ + 1
            else:
                return 1

        else:
            return 1


