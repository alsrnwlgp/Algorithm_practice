from sys import stdin
read = stdin.readline
N = int(read())
maxdp = [0]*3
mindp = [0]*3
for _ in range(N):
    a, b, c = map(int, read().split())
    maxdp[0], maxdp[1], maxdp[2] = a + max(maxdp[:2]), b + max(maxdp), c + max(maxdp[1:])
    mindp[0], mindp[1], mindp[2] = a + min(mindp[:2]), b + min(mindp), c + min(mindp[1:])
print(max(maxdp), min(mindp))
