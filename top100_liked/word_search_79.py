class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start_pnt = [];
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    start_pnt.append((i, j))

        if len(start_pnt) == 0: return False
        for i, j in start_pnt:
            if self.dfs(board, 0, i, j, word): return True
        return False

    def dfs(self, board, count, i, j, word):
        if count == len(word): return True
        if i < 0 or i >= len(board) or j >= len(board[i]) or j < 0: return False
        if word[count] != board[i][j]: return False

        save = board[i][j]
        board[i][j] = " "
        #         after saving, the cell is set to empty so the dfs can't be back to the cell
        isFound = self.dfs(board, count + 1, i + 1, j, word) or self.dfs(board, count + 1, i, j + 1, word) or self.dfs(
            board, count + 1, i - 1, j, word) or self.dfs(board, count + 1, i, j - 1, word)

        board[i][j] = save

        return isFound

