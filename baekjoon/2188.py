n, m = map(int, input().split())
wants = [[] for _ in range(n+1)]
home = [0 for _ in range(m+1)]
for i in range(1, n+1):
  wants[i] = list(map(int, input().split()))[1:]


def dfs(cow):
  if visited[cow]:
    return False
  visited[cow] = True
  for i in wants[cow]:
    if home[i] == 0 or dfs(home[i]):
      home[i] = cow
      return True
  return False


for cow in range(1, n+1):
  visited = [False for _ in range(n+1)]
  dfs(cow)
print(sum(list(map(lambda x: 1 if x>0 else 0, home))))
