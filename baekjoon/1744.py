n = int(input())
nums = sorted([int(input()) for _ in range(n)])
zero, one = 0, 0
neg = []
pos = []
ans = 0
for num in nums:
  if num == 0:
    zero += 1
  if num == 1:
    one += 1
  if num < 0:
    neg.append(num)
  if num > 1:
    pos.append(num)
if len(neg)%2 == 0:
  for i in range(0, len(neg), 2):
    ans += neg[i]*neg[i+1]
else:
  for i in range(0, len(neg)-1, 2):
    ans += neg[i]*neg[i+1]
  if zero == 0:
    ans += neg[-1]
ans += one
if len(pos)%2==0:
  for i in range(0,len(pos),2):
    ans += pos[i]*pos[i+1]
else:
  ans += pos[0]
  for i in range(1,len(pos),2):
    ans += pos[i]*pos[i+1]
print(ans)
