n = int(input())
cranes = sorted(list(map(int, input().split())), reverse = True)
m = int(input())
boxs = sorted(list(map(int, input().split())), reverse=True)
if cranes[0] < boxs[0]:
  print(-1)
else:
  count = 0
  while boxs:
    for c in cranes:
      for b in boxs:
        if c >= b:
          boxs.remove(b)
          break
    count += 1
  print(count)
