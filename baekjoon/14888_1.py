import sys
def cal(res, i, pl, mi, mu, di):
    global max_, min_, N, nums
    if N == i:
        max_ = max(max_, res)
        min_ = min(min_, res)
        return
    if pl:
        cal(res+nums[i], i+1, pl-1, mi, mu, di)
    if mi:
        cal(res-nums[i], i+1, pl, mi-1, mu, di)
    if mu:
        cal(res*nums[i], i+1, pl, mi, mu-1, di)
    if di:
        if res >= 0:
            cal(res//nums[i], i+1, pl, mi, mu, di-1)
        else:
            res = -res
            res //= nums[i]
            res = -res
            cal(res, i+1, pl, mi, mu, di-1)
N = int(input())
nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())
max_ = -sys.maxsize
min_ = sys.maxsize
cal(nums[1], 1, pl, mi, mu, di)
print(max_)
print(min_)