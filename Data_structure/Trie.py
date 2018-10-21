class Tries(object):
    def __init__(self):
        self.tries = {}
        self.counter = 0

    def make_tries(self, wordList):
        for i, word in enumerate(wordList):
            curr_dict = self.tries
            for c in word:
                curr_dict = curr_dict.setdefault(c, {})
            else:
                curr_dict['end'] = i
            self.counter += 1

    def search(self, word):
        curr_dict = self.tries
        for c in word:
            if c in curr_dict:
                curr_dict = curr_dict[c]
            else:
                return False
        else:
            if 'end' in curr_dict:
                return curr_dict['end']
            else:
                return False

    def insert(self, word):
        curr_dict = self.tries
        for c in word:
            curr_dict = curr_dict.setdefault(c, {})
        else:
            curr_dict['end'] = self.counter
            self.counter += 1




wordList = ['han', 'xu', 'fight']
tries = Tries()
tries.make_tries(wordList)
tries.insert('hand')
tries.insert('hands')
print tries.tries