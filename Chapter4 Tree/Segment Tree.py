# Segment Tree is a basically a binary tree used for storing the intervals or segments.
# Each node in the Segment Tree represents an interval.

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """

        # helper function to create the tree from input array
        def createTree(nums, l, r):

            # base case
            if l > r:
                return None

            # leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = (l + r) // 2

            root = Node(l, r)

            # recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)

            # Total stores the sum of all leaves under root
            # i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total

            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """

        # Helper function to update a value
        def updateVal(root, i, val):

            # Base case. The actual value will be updated in a leaf.
            # The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            # If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)

            # Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)

            # Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total

            return root.total

        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        # Helper function to calculate range sum
        def rangeSum(root, i, j):

            # If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            # If end of the range is less than the mid, the entire interval lies
            # in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)

            # If start of the interval is greater than mid, the entire inteval lies
            # in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)

            # Otherwise, the interval is split. So we calculate the sum recursively,
            # by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)


class Treenode(object):
    def __init__(self, start, end, sums=0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sums = sums


class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def buildSegementTree(nums, start, end):
            # if start > end: return None
            if start == end:
                return Treenode(start, end, nums[start])
            root = Treenode(start, end)
            mid = start + (end - start) / 2
            root.left = buildSegementTree(nums, start, mid)
            root.right = buildSegementTree(nums, mid + 1, end)
            if root.left:
                root.sums += root.left.sums
            if root.right:
                root.sums += root.right.sums
            return root

        self.root = buildSegementTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def update_tree (root):
            if root.start == root.end == i:
                prev = root.sums
                root.sums = val
                return val - prev

            mid = root.start + (root.end - root.start) / 2
            if mid >= i:
                diff = update_tree(root.left)
            else:
                diff = update_tree(root.right)
            root.sums += diff
            return diff
        update_tree(self.root)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangesum(root, i, j):
            if i == root.start and j == root.end:
                return root.sums

            mid = root.start + (root.end - root.start)/2
            if j <= mid:
                return rangesum(root.left, i, j)
            elif i > mid:
                return rangesum(root.right, i, j)
            else:
                return rangesum(root.left, i, mid) + rangesum(root.right, mid + 1, j)
        return rangesum(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
nums = range(10)
print sum(nums)
arr1 = NumArray(nums)
arr2 = NumArray2(nums)

print arr2.sumRange(4,8)
print arr1.sumRange(4,8)