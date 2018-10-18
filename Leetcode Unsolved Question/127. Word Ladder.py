# coding=utf-8

# 我虽然写出来了单向的BFS，但是其实双向的BFS更快，更好。
# 如果是单向的BFS，那么问题便是说如果search的话，最后会遍历太多的node
# 而如果是双向的BFS，那么就可以脱离这个问题来解决了。我们每次都选择更小
# 的那个set来开始，而每次我们都向前走一步而已.

# 最后的表现非常能说明问题，如果我每次都选择更大的set走，那么需要650ms
# 来process，但是如果反过来每次都选择更小的set走，竟然只需要96ms。前后
# 将近差了一倍。

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList: return 0
        front, back = set([beginWord]), set([endWord])
        word_lens = len(beginWord)
        lens = 1
        while front:
            lens += 1
            next_front = set()
            for word in front:
                for i in xrange(word_lens):
                    for c in string.lowercase:
                        if c == word[i]: continue
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in back:
                            return lens
                        if new_word in wordList:
                            wordList.remove(new_word)
                            next_front.add(new_word)
            # print next_front, front
            front = next_front
            if len(front) > len(back):
                front, back = back, front
        return 0