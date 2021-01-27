def greatest_common_divisor(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def least_common_multiple(num1, num2):
    gcd = greatest_common_divisor(num1, num2)
    return num1 * num2 // gcd


n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    print(least_common_multiple(num1, num2))
