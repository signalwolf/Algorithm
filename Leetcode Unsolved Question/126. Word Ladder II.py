# coding=utf-8

# 这道题之前的题目是word laddar I，leetcode127，不同之处在于说127是要求length而126要求path
# 所以如何求path便变成了一个问题。


#  在这里我使用的还是原先的方法，在单词的后面记录其path，然后最后combine它。
#  但是还是很多细节没有考虑，首先我们不能assume 到任意点的path 只有一个，
#  所以需要用defaultdict
#  另一个方面在于我们在删除的时候不能每次发现新词就删除，在同一层上面，它也可以
#  继续向前进

# DFS 的方法也要看看

from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList: return []
        wordList.remove(endWord)
        front, back = defaultdict(list), defaultdict(list)
        front[beginWord] = [[beginWord]]
        back[endWord] = [[endWord]]
        base = ord('a')
        res = []
        while front:
            next_front = defaultdict(list)
            delete_list = set()
            for word in front.keys():
                paths = front[word]
                for i in xrange(len(word)):
                    for j in xrange(26):
                        new_char = chr(base + j)
                        if new_char == word[i]: continue
                        new_word = word[:i] + new_char + word[i + 1:]

                        if new_word in back:
                            for path in paths:
                                for back_path in back[new_word]:
                                    if path[0] == beginWord:
                                        res.append(path + back_path[::-1])
                                    else:
                                        res.append(back_path + path[::-1])
                        if new_word in wordList:
                            for path in paths:
                                next_front[new_word].append(path + [new_word])
                            delete_list.add(new_word)
            for word in delete_list:
                wordList.remove(word)
            front = next_front
            if res:
                return res
            if len(front) > len(back):
                front, back = back, front
        return res