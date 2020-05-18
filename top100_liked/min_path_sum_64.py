class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mul = len(grid) * len(grid[0])
        downs = len(grid) - 1;
        rights = len(grid[0]) - 1
        alls = downs + rights;
        save_dic = {};
        updated_dic = {}
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                save_dic[(i, j)] = grid[i][j]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    updated_dic[(i, j)] = save_dic[(i, j)]
                else:
                    if i == len(grid) - 1:
                        updated_dic[(i, j)] = save_dic[(i, j)] + updated_dic[(i, j + 1)]
                        continue
                    if j == len(grid[0]) - 1:
                        updated_dic[(i, j)] = save_dic[(i, j)] + updated_dic[(i + 1, j)]
                        continue
                    updated_dic[(i, j)] = save_dic[(i, j)] + min(updated_dic[(i + 1, j)], updated_dic[(i, j + 1)])

        return updated_dic[(0, 0)]
