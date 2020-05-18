class Solution:
    def dfs(self, index, candidates, target, path, list_):
        if target < 0: return
        if target == 0:
            list_.append(path)

        for i in range(index, len(candidates)):
            self.dfs(i, candidates, (target - candidates[i]), (path + [candidates[i]]), list_)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        set_list = [];
        #         final answer sets
        path = []
        #         path save
        self.dfs(0, candidates, target, path, set_list)
        return set_list