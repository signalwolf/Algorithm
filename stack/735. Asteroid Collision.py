# too many coner case, think before you write sth.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids: return asteroids
        stack = [asteroids[0]]
        for i in xrange(1, len(asteroids)):
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                new = asteroids[i]
                while stack and stack[-1] > 0 and stack[-1] < abs(new):
                    stack.pop()

                if stack and stack[-1] == abs(new):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(new)
            else:
                stack.append(asteroids[i])
        return stack