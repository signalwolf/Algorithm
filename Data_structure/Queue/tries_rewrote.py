
class Tries(object):

    def __init__(self):
        self.tries = {}

    def buildTries(self, strings):
        for string in strings:
            curr_dicts = self.tries
            for letter in string:
                curr_dicts = curr_dicts.setdefault(letter, {})
            else:
                curr_dicts['end'] = 'end'

    def insert(self, string):
        curr_dict = self.tries
        for letter in string:
            curr_dict = curr_dict.setdefault(letter, {})
        else:
            curr_dict['end'] = 'end'

    def remove(self, string):
        self.delete(string, 0, self.tries)

#     def delete(self, string, index, curr_dict):




T = Tries()
wordList = ['han', 'xu', 'fight']
tries = Tries()
tries.buildTries(wordList)
print tries.tries
tries.insert('hand')
tries.insert('hands')
print tries.tries
# tries.remove('hand')
# tries.remove('han')
print tries.tries
# tries.remove('hands')
print tries.tries