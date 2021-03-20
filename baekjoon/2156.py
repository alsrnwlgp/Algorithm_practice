import sys
read = sys.stdin.readline

n = int(read())
X = []
for _ in range(n):
    X.append(int(read()))
dp = [0]*n
for i in range(n):
    if i == 0:
        dp[i] = X[i]
    elif i == 1:
        dp[i] = X[i] + X[i-1]
    elif i == 2:
        dp[i] = max(dp[i-1], X[i]+max(dp[i-2], X[i-1]))
    else:
        dp[i] = max(dp[i-1], X[i]+max(dp[i-2], dp[i-3]+X[i-1]))
print(dp[-1])
