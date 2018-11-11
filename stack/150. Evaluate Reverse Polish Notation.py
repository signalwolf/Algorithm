class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            # print stack
            if token in ['+','-','*','/']:
                right = (stack.pop())
                left = (stack.pop())
                if token == '+':
                    stack.append(left + right)
                if token == '-':
                    stack.append(left - right)
                if token == '*':
                    stack.append(left * right)
                if token == '/':
                    if left / right < 0:
                        stack.append( -1 * (abs(left)/abs(right)))
                    else:
                        stack.append(left /right)
            else:
                stack.append(int(token))
        return stack[0]