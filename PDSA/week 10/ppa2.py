def kmp_fail(p):
    m = len(p)
    fail = [0 for i in range(m)]
    j,k = 1,0
    while j < m:
        if p[j] == p[k]: 
            fail[j] = k+1
            j,k = j+1,k+1
        elif k > 0:
            k = fail[k-1]
        else:
            j = j+1
    return(fail)

def PrefixMatch(s):
    res=[]
    if len(s)==0:
        return res
    m = kmp_fail(s)
    for i in m:
        if i != 0:
            res.append(s[:i])
    ss = list(set(res))
    return ss
