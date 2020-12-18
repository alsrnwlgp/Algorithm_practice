def check_table(table):
    n = len(table)
    ans = 1
    for i in range(n):
        candies = table[i]
        print(candies)
        length = 1
        for j in range(n-1):
            if candies[j] == candies[j+1]:
                length += 1
                if ans < length:
                    ans = length
            else:
                length = 1
    for i in range(n):
        candies = table
        print(candies)
        length = 1
        for j in range(n-1):
            if candies[j] == candies[j+1]:
                length += 1
                if ans < length:
                    ans = length
            else:
                length = 1
    return ans
# def check_table(a):
#     n = len(a)
#     ans = 1
#     for i in range(n):
#         cnt = 1
#         for j in range(1, n):
#             if a[i][j] == a[i][j-1]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             if ans < cnt:
#                 ans = cnt
#         cnt = 1
#         for j in range(1, n):
#             if a[j][i] == a[j-1][i]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             if ans < cnt:
#                 ans = cnt
#     return ans

n = int(input())
table = [list(input()) for _ in range(n)]
# ans = 0
# for i in range(n):
#     for j in range(n):
#         if i < n-1:
#             table[i][j], table[i+1][j] = table[i+1][j], table[i][j]
#             ans = max(ans, check_table(table))
#             table[i][j], table[i+1][j] = table[i+1][j], table[i][j]
#         if j < n-1:
#             table[i][j], table[i][j+1] = table[i][j+1], table[i][j]
#             ans = max(ans, check_table(table))
#             table[i][j], table[i][j+1] = table[i][j+1], table[i][j]
# print(ans)
check_table(table)
