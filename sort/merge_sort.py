# coding=utf-8


from random import randint

def quick_sort(array, start, end):
    def partition():
        base = array[start]
        left, right = start + 1, end
        #done = False
        while left < right:
            while left <= right and array[left] <= base:
                left += 1

            while right >= left and array[right] > base:
                right -= 1

            if left < right:
                array[left], array[right] = array[right], array[left]
            else:
                if left - right != 1: print left - right

        array[start], array[right] = array[right], array[start]
        return right

    if start < end:
        mid = partition()
        quick_sort(array, start, mid - 1)
        quick_sort(array, mid + 1, end)

def merge_sort(array, start, end):
    if start >= end: return []
    if start == end - 1: return [array[start]]
    mid = start + (end - start) / 2
    left = merge_sort(array, start, mid)
    right = merge_sort(array, mid, end)
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    if i == len(left): res += right[j:]
    if j == len(right): res += left[i:]
    return res

# 我觉得这个是selection sort，每次遍历我都在寻找第一小，第二小的number
def selection_sort(array):
    res = array[::]
    for i in xrange(len(res)):
        for j in xrange(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    return res

# 这个不知道是什么sort
def temp_sort(array):
    res = [None] * len(array)
    for i in xrange(len(array)):
        index = 0
        for j in xrange(len(array)):
            if array[j] < array[i]:
                index += 1
        while res[index] != None:
            index += 1
        res[index] = array[i]
    # print res
    return res

# Bubble sort就是通过不断的交换使得最小的或者最大的到list的最后
def bubble_sort(array):
    n = len(array)
    for i in xrange(n):
        for j in xrange(0,n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# def quick_sort_with_random (array):


def main():
    array =  arr_generator(1000, 0, 100)
    # print array
    copy = array[:]
    merge = merge_sort(copy, 0, len(copy))
    print merge == sorted(array)
    copy = array[:]
    quick_sort(copy, 0, len(copy) - 1)
    # print copy
    print copy == sorted(copy)

    copy = array[:]
    bubble = bubble_sort(copy)
    # print bubble
    # print sorted(array)
    print bubble == sorted(array)

def arr_generator(n, start, end):
    res = []
    for i in xrange(n):
        res.append(randint(start, end))
    return res

if __name__ == '__main__':
    main()