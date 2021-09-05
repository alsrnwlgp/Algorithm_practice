from sys import stdin
read = stdin.readline
n, s = map(int, read().split())
li = list(map(int, read().split()))
for i in range(1, len(li)):
    li[i] += li[i-1]
ans = 1000001
start, end = 0, 1
while start < n-1 and end < n :
    if li[end] - li[start] >= s:
        ans = min(ans, end - start)
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1
if ans == 1000001:
    print(0)
else:
    print(ans)
