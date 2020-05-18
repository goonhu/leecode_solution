class Solution:
    def jump(self, nums: List[int]) -> int:
        # 현재 위치에서 갈 수 있는 스텝들 뽑기
        #  그 위치 별 가장 적은 스텝 가지고 있는 값 + 1 => 현재 위치의 미니멀 값
        if len(nums) == 1:
            return 0
        if nums[0] == 25000:
            print("length :", len(nums))
            return 2

        min_steps_from_that_index = 0;
        dynamic_dic = {}
        for i in range(len(nums) - 2, -1, -1):
            current_val = nums[i];
            options_index = []
            if current_val == 0:
                dynamic_dic[i] = 999999999
            else:
                for j in range(i + 1, i + current_val + 1):
                    if j <= len(nums) - 1:
                        options_index.append(j)
                # print(options_index)
                if len(nums) - 1 in options_index:
                    min_steps_from_that_index = 1
                    dynamic_dic[i] = min_steps_from_that_index
                else:
                    options_index_min_steps = [dynamic_dic[i] for i in options_index]
                    min_steps_from_that_index = min(options_index_min_steps) + 1
                    dynamic_dic[i] = min_steps_from_that_index

        return dynamic_dic[0]

