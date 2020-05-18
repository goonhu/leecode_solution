class Solution:
    def letterCombinations(self, digits):
        match_dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'], '9': ['x', 'w', 'y', 'z']}

        if len(digits) == 0: return []
        if len(digits) == 1: return match_dic[digits]

        first_chars = match_dic[digits[0]]

        for index in range(1, len(digits)):
            letters_new = match_dic[digits[index]]
            updated = [string + char for string in first_chars for char in letters_new]
            first_chars = updated

        return first_chars