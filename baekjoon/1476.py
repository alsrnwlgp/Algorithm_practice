import sys

max_value = 15*28*19

a, b, c = map(int, input().split())

for i in range(max_value//15):
    for j in range(max_value//28):
        for k in range(max_value//19):
            if 15*i + a == 28*j + b and 28*j + b == 19*k + c:
                print(15*i + a)
                sys.exit(0)