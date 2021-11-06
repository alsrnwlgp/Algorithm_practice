import sys
input = sys.stdin.readline
n, m = map(int, input().split())
people = [[] for _ in range(n+1)]
work = [0 for _ in range(m+1)]
for i in range(1, n+1):
  people[i] = list(map(int, input().split()))[1:]

def dfs(p):
  if visit[p]:
    return False
  visit[p] = True
  for w in people[p]:
    if work[w] == p:
      continue
    if work[w] == 0 or dfs(work[w]):
      work[w] = p
      return True
  return False


count = 0
for i in range(1, n+1):
  for _ in range(2):
    visit = [False for _ in range(n+1)]
    if dfs(i):
      count += 1
print(count)
