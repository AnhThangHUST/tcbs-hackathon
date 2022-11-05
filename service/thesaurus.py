from storage import repository_executor


def createThesaurus():
    query_res = repository_executor.getAllSynonym()
    thesaurus = {}
    for r in query_res:
        r.synonym.replace(" ", "")
        words = r.synonym.split(",")
        words.append(r.word)
        words_set = set(words)
        for w in words:
            if w not in thesaurus:
                thesaurus[w] = words_set
            else:
                thesaurus[w] = thesaurus[w].union(words_set)
    return thesaurus
