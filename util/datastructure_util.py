import json

from string import punctuation

special_characters = set(punctuation)


def serializeList(l):
    return json.dumps(l, default=lambda o: o.__dict__, indent=4)


def processSentence(sentence):
    sentence = sentence.lower().replace("\n", " ")
    sentence = " ".join(sentence.split())
    l = len(sentence)
    i = 0
    while i < l:
        if sentence[i] == ' ' or sentence[i] in special_characters:
            i += 1
        else:
            break
    sentence = sentence[i:]
    l = len(sentence)
    i = l - 1
    while i >= 0:
        if sentence[i] == ' ' or sentence[i] in special_characters:
            i -= 1
        else:
            break
    sentence = sentence[:i + 1]

    return sentence
