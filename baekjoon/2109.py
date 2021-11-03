import heapq
n = int(input())
works = []
for _ in range(n):
  works.append(tuple(map(int, input().split())))
works = sorted(works, key=lambda x: x[1])
sums = []
preday = works[0][1]
for pay, day in works:
  if preday != day:
    while preday < len(sums):
      heapq.heappop(sums)
  heapq.heappush(sums, pay)
  preday = day
print(sum(sums))
