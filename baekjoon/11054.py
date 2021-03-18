n = int(input())
n_list = list(map(int, input().split()))
increasing_dp = [1]*n
decreasing_dp = [1]*n
for i in range(n):
    for j in range(i):
        if n_list[j] < n_list[i]:
            increasing_dp[i] = max(increasing_dp[i], increasing_dp[j]+1)
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if n_list[j] < n_list[i]:
            decreasing_dp[i] = max(decreasing_dp[i], decreasing_dp[j]+1)
dp = [sum(x)-1 for x in zip(increasing_dp, decreasing_dp)]
print(max(dp))

