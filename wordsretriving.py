def load():
    result = list()

    fl = 'index.csv'
    fname = open(fl)


    # retrieve level title
    for line in fname:
        filelst = list()
        words = line.split(';')
        filelst.extend(words)

        dictionlst = list()

        wordlst = filelst[0]
        allwords = open(wordlst)

        # retrieve french and english words pair
        for word in allwords:
            word = word.rstrip()
            word = word.split(';')
            wordcouple = ((word[0], word[1]))
            dictionlst.append(wordcouple)
        print(dictionlst)
        result.append((filelst[1], dictionlst))

    return result
