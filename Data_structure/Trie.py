class Tries(object):
    def __init__(self):
        self.tries = {}

    def make_tries(self, wordList):
        for i, word in enumerate(wordList):
            curr_dict = self.tries
            for c in word:
                curr_dict = curr_dict.setdefault(c, {})
            else:
                curr_dict['end'] = i

    def search(self, word):
        curr_dict = self.tries
        for c in word:
            if c in curr_dict:
                curr_dict = curr_dict[c]
            else:
                return False
        else:
            



wordList = ['han', 'xu', 'fight']
tries = Tries()
tries.make_tries(wordList)
print tries.tries
