# coding=utf-8
# 1. 如何在python code中输入中文字：# coding=utf-8
#       python以及pycharm的default的编码是ASCII， 而中文是UTF-8,故而该代码后能work
# 2. 关于BFS的流程，有两种方式，一种是在BFS的neighbor环节update visited的dictionary, 另一种是在queue的pop的环节来处理。
# 在performance上，在处理neighbor的时候处理是更快的。但是在算法上，很多算法是在外面处理的
# 3. Question: does empty dictionary consider to be False?
# 4. 思考方法：
#    面对复杂的问题，思考一个更加简单的问题并且从中得到思路。例如310。
# 5. 不要忘记了initial node 的方法
# 6. Tree delete node 的方法忘记了
# 7. Quick sort中的random shuffle
# 8. Very careful about 0, it is False/None as well.
# 9. 使用while语句来遍历整个node的情况
# 10. Union Find.
# 11. Quick sort的in place的算法以及randomized的方法：
#       in place的算法就是
#           先选定start为它的pivot node, 然后建立两个指针，一个在左一个在右。
#           对于左边的指针，如果当前node的值比pivot node小，那么不变，向前移动否则的话就是stop；终点在于遇上right
#           同理右边的指针在做的事情就是看它的node是否比pivot node 大，如果不大的话就要停下，终点在于遇上left
#           当左右两个指针都停下的时候，此时有两种情况，
#               一：左指针还在右指针的左边，此时说明还有node没有被分边。故而互换后继续。如果是相差为一的话，也是需要互换的。
#               二：左指针与右指针相遇了（只有可能在start = end - 1 情况下出现）：
#                   此时left 左边的node都是小于pivot的，右边的node都是大于pivot的。
#                   而left，right的出循环条件导致了情况不可能出现。（left循环：left > right 或 A[left] >= A[pivot];
#                   Right: right < left or A[right] < A[pivot]. 故而如果要求left == right，那么是不可能出现的)
#               出现的条件在length == 2时，[1, 2] --> left == right = 1, left < right is False, so right = 1.
#               then swap start with right ---> [2, 1]. Wrong result, 故而要求在left == right时先互换一次后再在外面
#               互换。
#               三：左指针在右指针的右边，此时说明已经pass了，并且其实这时候left = right - 1
#          在出循环时，right指向了第一个小于pivot的点，left指向了第一个大于pivot的点。故而会pivot的index就是right的值。因为整个left
#          都要向前移动。故而继续下去的分法就是，start, right (not include), right + 1, end
#       Randomization的算法：
#           在每次partition之前，我们先将start 处的值与random gengerate的pivot的node的值互换。之后直接使用partitoon就好
#       写来写去，还是有错误，在sort的时候一定要用end 包含的模式。