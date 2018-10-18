

my_answer = [["magic","manic","mania","maria","marta","marty","party","parry","perry","peary","pearl"],["magic","manic","mania","maria","marta","marty","marry","parry","perry","peary","pearl"],["magic","manic","mania","maria","marta","marty","marry","merry","perry","peary","pearl"],["magic","manic","mania","maria","maris","paris","parks","perks","peaks","pears","pearl"],["magic","manic","mania","maria","maris","marks","parks","perks","peaks","pears","pearl"]]
expected_answer = [["magic","manic","mania","maria","marta","marty","party","parry","perry","peary","pearl"],["magic","manic","mania","maria","maris","paris","parks","perks","peaks","pears","pearl"],["magic","manic","mania","maria","marta","marty","marry","merry","perry","peary","pearl"],["magic","manic","mania","maria","marta","marty","marry","parry","perry","peary","pearl"],["magic","manic","mania","maria","maris","marks","parks","perks","peaks","pears","pearl"]]

my_answer = my_answer
expected_answer = expected_answer

for answers in my_answer:
    if answers in expected_answer:
        expected_answer.pop(expected_answer.index(answers))

for i in my_answer:
    print i

print expected_answer