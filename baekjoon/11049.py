import sys
read = sys.stdin.readline
MAX = sys.maxsize
N = int(read())
row = []
for i in range(N):
    a, b = map(int, read().split())
    if i == 0:
        row.append(a)
        row.append(b)
    else:
        row.append(b)
dp = [[MAX]*N for _ in range(N)]
for d in range(0, N):
    for i in range(0, N-d):
        j = i + d
        if i == j:
            dp[i][j] = 0
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + row[i]*row[k+1]*row[j+1])
print(dp[0][N-1])
