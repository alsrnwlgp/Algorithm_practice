from itertools import permutations
N = int(input())
nums = list(map(int, input().split()))
tmp = list(map(int, input().split()))
opers = []
for i, n in enumerate(tmp):
    for _ in range(n):
        opers.append(i)
Max = -1000000000
Min = 1000000000
for oper_li in list(set(permutations(opers, N-1))):
    ans = nums[0]
    for i, oper in enumerate(oper_li):
        if oper == 0:
            ans += nums[i+1]
        if oper == 1:
            ans -= nums[i+1]
        if oper == 2:
            ans *= nums[i+1]
        if oper == 3:
            if ans >= 0:
                ans //= nums[i+1]
            else:
                ans = -ans
                ans //= nums[i+1]
                ans = -ans
    Max = max(Max, ans)
    Min = min(Min, ans)
print(Max)
print(Min)
