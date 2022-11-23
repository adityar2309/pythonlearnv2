def kthLargest(arr, k):
    return fast(arr, 0, len(arr), k)
def Medianofmedian(L):
    if(len(L)<=5):
        L.sort()
        return(L[len(L)//2])
    M=[]
    for i in range(0,len(L),5):
        x=L[i:i+5]
        x.sort()
        M.append(x[len(x)//2])
    return (Medianofmedian(M))
def fast(L,l,r,k):
    if(k<l) and (k>r-l):
        return None
    pivot=Medianofmedian(L[l:r])
    pivotpos=min([i for i in range(l,r) if L[i]==pivot])
    (L[l],L[pivotpos])=(L[pivotpos],L[l])
    (pivot,lower,upper)=(L[l],l+1,l+1)
    for i in range(l+1,r):
        if L[i]<pivot:
            upper=upper+1
        else:
            (L[i],L[lower])=(L[lower],L[i])
            (lower,upper)=(lower+1,upper+1)
    (L[l],L[lower-1])=(L[lower-1],L[l])
    lower=lower-1
    lowerlen=lower-l
    if k<=lowerlen:
        return(fast(L,l,lower,k))
    elif k==(lowerlen+1):
        return(L[lower])
    else:
        return(fast(L,lower+1,r,k-(lowerlen+1)))
