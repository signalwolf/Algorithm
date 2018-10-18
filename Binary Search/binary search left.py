# coding=utf-8

# 本以为binary search没有问题，但是一写还是有bug
# 在找左边和右边的时候注意考虑边界条件。
# [1,1,1,1,1,2,3] --> 最后的start = 0, end = 1. 故而如果先check start，回的便是0，先check end回复为1
# [1,2,3,3,3,3,3] --> 最后的start = 2, end = 6. 故而如果先check start，回复的便是5，先check end回复为6
# 需要特别注意。

# 同时要特别注意Bisect的问题，它是考虑将某个数值插入到sorted list中的位置，故而left是没有问题的
# 但是right 要注意它是多了1的
# 例如：[1,1,2,3] bisect left(1) = 0, bisect right (1) = 2, bisect right (2) = 3, bisect right(3) = 4

import random
from bisect import bisect_left, bisect_right


def input_generator(n):
    exam = range(1, n)
    for i in xrange(3):
        exam += [random.randint(1, n -1)] * random.randint(1,5)
    exam.sort()
    return exam

def expected_solution(exam):
    n = exam[-1]
    expected_left = []
    expected_right = []
    for i in xrange(1, n + 1):
        expected_left.append(bisect_left(exam, i))
        expected_right.append(bisect_right(exam, i))
    return expected_left, expected_right

n = 5
input = input_generator(n)
input = [1, 1, 2, 3]
# print input
expected_left, expected_right =  expected_solution(input)

def my_binary_search(arr, target, left = True):
    if len(arr) == 0: return None
    start, end = 0, len(arr) - 1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if arr[mid] > target:
            end = mid
        elif arr[mid] < target:
            start = mid
        else:
            if left: end = mid
            else: start = mid
    if left:
        if arr[start] == target: return start
        if arr[end] == target: return end
    else:
        if arr[end] == target: return end
        if arr[start] == target: return start
    return None

my_ans_left = []
my_ans_right = []
for i in xrange(1, input[-1] + 1):
    my_ans_left.append(my_binary_search(input, i))
    my_ans_right.append(my_binary_search(input,i, False) + 1)


print my_ans_left == expected_left
print my_ans_right == expected_right
print expected_right

