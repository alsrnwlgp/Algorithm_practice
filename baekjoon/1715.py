import heapq
n = int(input())
h = []
for _ in range(n):
  heapq.heappush(h, int(input()))
ans = 0
while len(h) > 1:
  new = heapq.heappop(h) + heapq.heappop(h)
  heapq.heappush(h, new)
  ans += new
print(ans)
