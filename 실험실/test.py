a, b = map(int, input().split())
r = a
# 나머지에 10을 곱한 값을 7로 나눴을 때의 몫을 순서대로 적는 것을 계속 반복

if a < b:
    print("0.", end="")

else:
    q = a // b
    r = a % b
    print(f'{q}.', end="")

for _ in range(0, 20):
    q = (r * 10) // b
    r = (r * 10) % b
    print(q, end="")