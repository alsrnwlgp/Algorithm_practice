n, m = map(int, input().split())
person = [[] for _ in range(n+1)]
work = [0 for _ in range(m+1)]
for i in range(1, n+1):
  person[i] = list(map(int, input().split()))[1:]

def dfs(start):
  if visit[start]:
    return False
  visit[start] = True
  for w in person[start]:
    if work[w] == 0 or dfs(work[w]):
      work[w] = start
      return True
  return False


count = 0
for i in range(1, n+1):
  visit = [False for _ in range(n+1)]
  if dfs(i):
    count += 1
print(count)
