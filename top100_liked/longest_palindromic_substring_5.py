

class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0: return ''
        #         this case, when the string is empty, need to be considered, or thinking of how the general solution covers this

        length = len(s)
        ans_options = {}
        current_longest = 0

        for index in range(0, len(s)):
            for j in range(length, index, -1):
                sliced_s = s[index:j]
                if sliced_s[::-1] == sliced_s:
                    ans_options[sliced_s] = len(sliced_s)
                    if len(sliced_s) >= current_longest: current_longest = len(sliced_s)

        reversed_dic = {j: i for i, j in ans_options.items()}
        return reversed_dic[current_longest]


