d = [[0]*10 for _ in range(101)]
mod = 1000000000
n = int(input())
for i in range(1, 10):
    d[1][i] = 1
for i in range(2, n+1):
    for j in range(0, 10):
        d[i][j] = 0
        if j >= 1:
            d[i][j] += d[i-1][j-1]
        if j <= 8:
            d[i][j] += d[i-1][j+1]
        d[i][j] %= mod
ans = sum(d[n]) % mod
print(ans)
