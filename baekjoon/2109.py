import heapq
n = int(input())
works = []
for _ in range(n):
  works.append(tuple(map(int, input().split())))
works = sorted(works, key=lambda x: x[1])
sums = []
for pay, day in works:
  heapq.heappush(sums, pay)
  if day < len(sums):
      heapq.heappop(sums)
print(sum(sums))
