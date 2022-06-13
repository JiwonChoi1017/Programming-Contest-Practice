import sys

# A - You should output ARC, though this is ABC.
# https://atcoder.jp/contests/abc255/tasks/abc255_a
r, c = map(int, sys.stdin.readline().split())
a = []

for _ in range(2):
    a.append(list(map(int, sys.stdin.readline().split())))

print(a[r - 1][c - 1])
