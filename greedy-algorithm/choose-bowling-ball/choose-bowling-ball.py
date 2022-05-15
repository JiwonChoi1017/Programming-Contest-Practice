import sys

# ボウリングボール選び
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

result = 0

for i in range(n):
    for j in range(i + 1, n):
        if li[i] != li[j]:
            result += 1

print(result)
