memo = {}
def constructWord(word, wordList):
    if word == '':
        return [[]]
    if word in memo.keys():
        return memo[word]
    totalwordlist = []
    for subword in wordList:
        if subword == word[:len(subword)]:
            subwordList = constructWord(word[len(subword):], wordList)
            totalwordlist.extend([[subword] + lst for lst in subwordList])
    memo[word] = totalwordlist
    return totalwordlist

