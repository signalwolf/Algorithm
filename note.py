# coding=utf-8
# 1. 如何在python code中输入中文字：# coding=utf-8
#       python以及pycharm的default的编码是ASCII， 而中文是UTF-8,故而该代码后能work
# 2. 关于BFS的流程，有两种方式，一种是在BFS的neighbor环节update visited的dictionary, 另一种是在queue的pop的环节来处理。
# 在performance上，在处理neighbor的时候处理是更快的。但是在算法上，很多算法是在外面处理的
# 