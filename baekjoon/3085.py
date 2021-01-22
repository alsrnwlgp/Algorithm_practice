# bruteforce 풀이

n = int(input())
candy_map = [list(input()) for _ in range(n)]


def find_max_candies(candy_map):
    max_len = 1
    for i in range(n):
        candy_array = candy_map[i]
        length = 1
        for j in range(1, n):
            if candy_array[j-1] == candy_array[j]:
                length += 1
                max_len = max(max_len, length)
            else:
                length = 1
    for i in range(n):
        candy_array = [l[i] for l in candy_map]
        length = 1
        for j in range(1, n):
            if candy_array[j-1] == candy_array[j]:
                length += 1
                max_len = max(max_len, length)
            else:
                length = 1
    return max_len


max_len = 1
for i in range(n):
    for j in range(n):
        if i < n-1:
            candy_map[i][j], candy_map[i+1][j] = candy_map[i+1][j], candy_map[i][j]
            max_len = max(max_len, find_max_candies(candy_map))
            candy_map[i][j], candy_map[i+1][j] = candy_map[i+1][j], candy_map[i][j]
        if j < n-1:
            candy_map[i][j], candy_map[i][j+1] = candy_map[i][j+1], candy_map[i][j]
            max_len = max(max_len, find_max_candies(candy_map))
            candy_map[i][j], candy_map[i][j+1] = candy_map[i][j+1], candy_map[i][j]
print(max_len)

