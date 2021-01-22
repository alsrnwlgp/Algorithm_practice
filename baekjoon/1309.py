n = int(input())

mod = 9901
D = [[0]*3 for _ in range(n+1)]
D[0][0] = 1
for i in range(1, n+1):
    D[i][0] = sum(D[i-1]) % mod
    D[i][1] = (D[i-1][0] + D[i-1][2]) % mod
    D[i][2] = (D[i-1][0] + D[i-1][1]) % mod
print(sum(D[n]) % mod)
