X = ' '+input()
Y = ' '+input()
n, m = len(X), len(Y)
dp = [[0]*m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if X[i] == Y[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])