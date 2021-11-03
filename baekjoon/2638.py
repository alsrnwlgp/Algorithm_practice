from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int, input().split())
mtr = [list(map(int, input().split())) for _ in range(n)]


def make_air(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.pop()
    mtr[x][y] = -1
    for i,j in zip(dx, dy):
      if 0<=x+i<n and 0<=y+j<m:
        if mtr[x+i][y+j] == 0:
          q.append((x+i, y+j))


make_air(0,0)


def is_decay_cheese(x, y):
  count = 0
  if mtr[x][y] == 1:
    for i, j in zip(dx,dy):
      if mtr[x+i][y+j] == -1:
        count += 1
  if count >= 2:
    return True
  return False


def cheese_to_air():
  decay_cheeses = []
  for i in range(n):
    for j in range(m):
      if is_decay_cheese(i, j):
        decay_cheeses.append((i,j))
  for i, j in decay_cheeses:
    make_air(i, j)


def is_all_air():
  for i in range(n):
    for j in range(m):
      if mtr[i][j] != -1:
        return False
  return True

count = 0
while not is_all_air():
  cheese_to_air()
  count += 1

print(count)
