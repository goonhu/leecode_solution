import re


class Solution:
    def isMatch(self, s, p):

        result = re.findall(p, s)
        if s in result:
            return True
        else:
            return False