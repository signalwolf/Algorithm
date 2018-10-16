# coding=utf-8

# 解决的问题：大数据量的情况下随机选择K 个数的情况。

# mainly used for randomly select from an huge amount of data which can't fit into the memory like
# facebook, google's request.

# time complexsity: O(n)

from random import randint

input_list = range(100000)
k = 10

def sampling(input_list, k):
    res = input_list[:k]
    for i in xrange(k, len(input_list)):
        rand_num = randint(0, i)
        if rand_num < k:
            res[rand_num] = input_list[i]
    return res

print sampling(input_list, k)

