import sys

# B - 1D Pawn
# https://atcoder.jp/contests/abc257/tasks/abc257_b
n, k, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))

for i in l:
    if a[i - 1] < n and a[i - 1] + 1 not in a:
        a[i - 1] += 1

print(*a)
