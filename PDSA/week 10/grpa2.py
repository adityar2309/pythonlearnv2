def FindPattern(T,P):
    last = {} # Preprocess
    for i in range(len(P)):
        if P[i] != '$':
            last[P[i]] = i
    poslist=[]
    i = 0 # Loop
    while i <= (len(T)-len(P)):
        matched,j = True,len(P)-1
        while j >= 0 and matched:
            if P[j] != '$':
                if T[i+j] != P[j]:
                    matched = False
            j = j - 1            
        if matched:
            poslist.append((i,T[i:i+len(P)]))
            i = i + 1
        else:
            j = j + 1
            if T[i+j] in last.keys():
                i = i + max(j-last[T[i+j]],1)
            else:
                i = i + 1
    return(poslist)
T = input()
P = input()
print(FindPattern(T,P))