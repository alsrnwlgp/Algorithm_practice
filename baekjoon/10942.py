import sys
read = sys.stdin.readline
N = int(read())
li = list(map(int, read().split()))
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if li[i] == li[i+1]:
        dp[i][i+1] = 1
for l in range(2, N):
    for i in range(N-l):
        if li[i] == li[i+l] and dp[i+1][i+l-1]:
            dp[i][i+l] = 1
for _ in range(int(read())):
    s, e = map(int, read().split())
    print(dp[s-1][e-1])
