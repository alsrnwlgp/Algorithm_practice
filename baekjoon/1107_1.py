import sys

n = int(input())
input()
not_button = input().split()


def available_channel(a: int) -> bool:
    a_list = list(str(a))
    for i in a_list:
        if i in not_button:
            return False
    return True


# button이 다 고장나면 +, -만 눈러서 이동
if len(not_button) == 10:
    print(n-100 if n >= 100 else 100-next)
    sys.exit(0)

ans = 0
a = b = n
# brute force
while True:
    if available_channel(a):
        ans += len(str(a))
        break
    if available_channel(b):
        ans += len(str(b))
        break
    a, b, ans = a-1, b+1, ans+1
ans = min(ans, n-100 if n >= 100 else 100-n)
print(ans)
sys.exit(0)
