#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    else:
        for i in sentence:
            return len(sentence), sentence[0]
