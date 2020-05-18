class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dic = {')': '('};
        stack = [];
        stack.append((-1, '')),
        result = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append((index, char))
            else:
                if dic[char] == stack[-1][1]:
                    stack.pop(-1)
                    result = max(result, index - stack[-1][0])
                else:
                    stack.append((index, char))
        return result



