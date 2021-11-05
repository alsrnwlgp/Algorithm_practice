import heapq
n = int(input())
hw = []
h = []
for _ in range(n):
  hw.append(tuple(map(int, input().split())))
hw.sort()
for d, s in hw:
  heapq.heappush(h, s)
  while d < len(h):
    heapq.heappop(h)
print(sum(h))
