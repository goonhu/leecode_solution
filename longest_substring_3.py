class Solution:
    def lengthOfLongestSubstring(self, s):
        h = {i: 0 for i in s};
        default = {}
        for each in s:
            h[each] += 1
        for each in list(h.keys()):
            default[each] = 1

        max_len = 0
        for index in range(0, len(s)):
            current_index = index
            check = {key: value for key, value in default.items()}
            while (current_index < len(s) and check[s[current_index]] != 0):
                check[s[current_index]] -= 1
                current_index += 1
            last_index = current_index
            sliced_ = s[index:last_index]
            if len(sliced_) > max_len: max_len = len(sliced_)

        return max_len