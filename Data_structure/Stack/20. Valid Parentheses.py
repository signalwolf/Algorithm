class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def match(c1, c2):
            if c1 + c2 == '()' or c1 + c2 == '[]' or c1 + c2 == '{}':
                return True
            else:
                return False

        # Three cases:
        # 1. matched always
        # 2. not match with prev one
        # 3. still not empty after all matched.
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)
            else:
                if stack and match(stack.pop(), char):
                    continue
                else:
                    return False
        return stack == []
