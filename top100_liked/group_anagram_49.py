class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_default = [];
        check = [False] * len(strs)
        for each in strs:
            strs_default.append(sorted(each))
        print(strs)
        print(strs_default)
        answers = []
        unique = set(map(tuple, strs_default))
        for i in range(0, len(strs)):
            if check[i] == False:
                temp = [];
                temp.append(strs[i]);
                check[i] = True
                for j in range(i + 1, len(strs)):
                    if strs_default[i] == strs_default[j]:
                        temp.append(strs[j]);
                        check[j] = True
                answers.append(temp)
            else:
                continue
        return answers
