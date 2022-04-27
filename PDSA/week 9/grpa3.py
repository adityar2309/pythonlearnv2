def LDS(L):
    n = len(L)
    LDSCount = [1]*n # LDS with respect to the index
    prev = [None]*n # previous value with respect to the index
    for i in range(n):
        preMax = L[0]
        for j in range(i):
            if L[j] > L[i] and LDSCount[j] > preMax:
                preMax, prev[i] = LDSCount[j], j
        LDSCount[i] = 1 + preMax # updating LDSCount
    mx = max(LDSCount) # count of LDS
    mxi = LDSCount.index(mx) # index of LDS

    # backtracking to get the sequence
    seq = []
    while mxi != None:
        seq.append(L[mxi])
        mxi = prev[mxi]
    return seq[::-1]
