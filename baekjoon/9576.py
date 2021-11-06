# 이분매칭으로 풀이 pypy3 사용
t = int(input())
while t:
  t -= 1
  n, m = map(int, input().split())
  wants = [0 for _ in range(m+1)]
  book = [0 for _ in range(n+1)]
  for i in range(1, m+1):
    wants[i] = tuple(map(int, input().split()))

  def dfs(start):
    if visited[start]:
      return False
    visited[start] = True
    for w in range(wants[start][0], wants[start][1]+1):
      if book[w] == 0 or dfs(book[w]):
        book[w] = start
        return True
    return False
    
  count = 0
  for i in range(1, m+1):
    visited = [False for _ in range(m+1)]
    if dfs(i):
      count += 1
  print(count)