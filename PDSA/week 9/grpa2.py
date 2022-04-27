def MaxCoinPath(M,x1,y1,x2,y2):
    MCP=[]
    # Create matrix same size of M and initialized with 0
    for i in range(len(M)):
        L = []
        for j in range(len(M[0])):
            L.append(0)
        MCP.append(L)
    # Initialize x1 row and y1 coloumn    
    MCP[x1][y1] = M[x1][y1]
    for i in range(y1+1,len(M[0])):
        MCP[x1][i]= MCP[x1][i-1] + M[x1][i]
    for i in range(x1+1,len(M)):
        MCP[i][y1]= MCP[i-1][y1] + M[i][y1]
 # calculate value for each cell
    for i in range(x1+1,len(M)):
        for j in range(y1+1,len(M[0])):
            MCP[i][j] = max(MCP[i-1][j],MCP[i][j-1]) + M[i][j]
    # return max coin value at x2,y2
    return MCP[x2][y2]


M = eval(input())
(x1,y1)=eval(input())
(x2,y2) = eval(input())
print(MaxCoinPath(M,x1,y1,x2,y2))\