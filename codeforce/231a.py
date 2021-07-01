from sys import stdin
read = stdin.readline
n = int(read())
ans = 0
for _ in range(n):
    if sum(map(int, read().split())) >= 2:
        ans += 1
print(ans)