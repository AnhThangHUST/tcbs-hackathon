import json

from string import punctuation

special_characters = set(punctuation)


def serializeList(l):
    return json.dumps([ob.__dict__ for ob in l])


def processSentence(word):
    l = len(word)
    i = 0
    while i < l:
        if word[i] == ' ' or word[i] in special_characters:
            i += 1
        else:
            break
    word = word[i:]
    l = len(word)
    i = l - 1
    while i >= 0:
        if word[i] == ' ' or word[i] in special_characters:
            i -= 1
        else:
            break
    word = word[:i + 1]
    return word
