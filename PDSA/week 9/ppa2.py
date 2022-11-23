def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index:index+1] + t[:index] + t[index+1:])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1:index+1] + t[0:1] + t[index+1:])
    return L__

def MaxProfit(Activity):
    n = len(Activity)
    act = tuplesort(Activity, 2)    
    MaxProfit = []
    for a in act:
        MaxProfit.append(a[3])
    for i in range(1, n):
        for j in range(0, i):
            if act[i][1] >= act[j][2] and MaxProfit[i] < MaxProfit[j] + act[i][3] + 1:
                MaxProfit[i] = MaxProfit[j] + act[i][3]
    return max(MaxProfit)
