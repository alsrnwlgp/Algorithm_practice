len_of_array = int(input())
sorted_list = list(map(int, input().split()))
goal_val = int(input())
sorted_list.sort()
pointer_a = 0
pointer_b = len_of_array - 1
ans = 0
while pointer_a < pointer_b:
    if sorted_list[pointer_a] + sorted_list[pointer_b] == goal_val:
        ans += 1
        pointer_a += 1
        pointer_b -= 1
        continue
    elif sorted_list[pointer_a] + sorted_list[pointer_b] < goal_val:
        pointer_a += 1
        continue
    else:
        pointer_b -= 1
        continue
print(ans)
