class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        key = len(word1);
        query = len(word2);
        dic = {};
        dic[(0, 0)] = 0

        for i in range(1, key + 1):
            dic[(i, 0)] = i
        for j in range(1, query + 1):
            dic[(0, j)] = j

        for i in range(1, key + 1):
            for j in range(1, query + 1):
                if word1[i - 1] == word2[j - 1]:
                    dic[(i, j)] = dic[(i - 1), (j - 1)]
                else:
                    dic[(i, j)] = min(dic[(i - 1, j)] + 1, dic[(i, j - 1)] + 1, dic[(i - 1, j - 1)] + 1)

        return dic[(key, query)]


