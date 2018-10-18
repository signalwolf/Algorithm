from random import randint

def quick_sort(array):
    if not array: return []
    if len(array) == 1: return [array[0]]
    left, right = [], []
    base = array[0]
    for i in xrange(1, len(array)):
        if array[i] > base:
            right.append(array[i])
        else:
            left.append(array[i])
    return quick_sort(left) + [base] + quick_sort(right)


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

def bubble_sort(array):
    res = array[::]
    for i in xrange(len(res)):
        for j in xrange(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    return res

# selection sort suitable for duplicated sets?
def selection_sort(array):
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


def main():
    array =  arr_generator(1000, 0, 100)
    # print array
    merge = merge_sort(array, 0, len(array))
    print merge == sorted(array)
    quick = quick_sort(array)
    print quick == sorted(array)
    bubble = bubble_sort(array)
    print bubble == sorted(array)
    # array = list(set(array))
    # array += [array[-5]]
    selection = selection_sort(array)
    # print selection == sorted(selection)
    print selection == sorted(array)

def arr_generator(n, start, end):
    res = []
    for i in xrange(n):
        res.append(randint(start, end))
    return res

if __name__ == '__main__':
    main()