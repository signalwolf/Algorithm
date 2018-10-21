# coding=utf-8
# 大概的意思就是说我们可以random产生一些点，然后判断是否满足条件。
# 例如我们要从产生一个圆上的随机的点，我们便可以在它的正方形内产生，这样就没有问题了。

# 例如Leetcode 478
from random import uniform


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        x = uniform(self.xc - self.radius, self.xc + self.radius)
        y = uniform(self.yc - self.radius, self.yc + self.radius)
        if ((x - self.xc) ** 2 + (y - self.yc) ** 2) > self.radius ** 2:
            return self.randPoint()
        else:
            return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()