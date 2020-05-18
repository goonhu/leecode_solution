class Solution:
    def isValid(self, s: str) -> bool:
        #         this is a classic queue, stack problem
        dic = {')': '(', '}': '{', ']': '['}
        stack = []

        if s == '': return True

        for each in s:
            if each in ['{', '[', '(']:
                stack.append(each)
            elif each in ['}', ']', ')']:
                if len(stack) != 0:
                    if dic[each] != stack[len(stack) - 1]:
                        print(stack)
                        return False
                    else:
                        stack.pop(len(stack) - 1)
                else:
                    return False
            else:
                return False

        if len(stack) != 0:
            return False
        else:
            return True