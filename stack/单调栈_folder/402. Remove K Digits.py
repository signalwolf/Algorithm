class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0: return num
        if len(num) == 0 or len(num) == k: return '0'
        thre = len(num) - k
        stack = []
        for n in num:
            while k and stack and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        return str(int(''.join(stack[:thre])))