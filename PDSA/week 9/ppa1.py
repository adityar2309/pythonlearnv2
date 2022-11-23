def MaxValue(Items,W):
    (m,n) = (len(Items),W)
    c = []
    for i in range(m+1):
        row = []
        for j in range(n+1):
            row.append(0)
        c.append(row.copy())
    for i in range(1,m+1):
        for w in range(1,n+1):
            if Items[i][0] > w:
                c[i][w] = c[i-1][w]
            else:
                c[i][w] = max(c[i-1][w],Items[i][1]+c[i-1][w-Items[i][0]])
    return(int(c[m][n]))
