import sys
len_of_list = int(input())
ph_of_solutions = list(map(int, input().split()))
ph_of_solutions.sort()
pointer_a = 0
pointer_b = len_of_list-1
min_absolute_ph = sys.maxsize
ans_solutions = []
while pointer_a < pointer_b:
    mix_ph = ph_of_solutions[pointer_a] + ph_of_solutions[pointer_b]
    if min_absolute_ph > abs(mix_ph):
        ans_solutions = [ph_of_solutions[pointer_a],
                         ph_of_solutions[pointer_b]]
        min_absolute_ph = abs(mix_ph)
    if mix_ph < 0:
        pointer_a += 1
    elif mix_ph > 0:
        pointer_b -= 1
    else:
        break
print(ans_solutions[0], ans_solutions[1])
