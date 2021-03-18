n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
W = [0]
V = [0]
for _ in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
for i in range(1, n+1):
    for max_w in range(1, k+1):
        if W[i] > max_w:
            dp[i][max_w] = dp[i-1][max_w]
        else:
            dp[i][max_w] = max(dp[i-1][max_w], V[i] + dp[i-1][max_w - W[i]])
print(dp[n][k])
