n = int(input())
li = sorted(list(map(int, input().split())))
sum_weight = 0
for i in li:
  if sum_weight+1 >= i:
    sum_weight += i
  else:
    break
print(sum_weight+1)
