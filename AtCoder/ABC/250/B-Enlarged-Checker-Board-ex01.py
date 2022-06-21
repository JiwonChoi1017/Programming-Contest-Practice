import sys

# B - Enlarged Checker Board
# https://atcoder.jp/contests/abc250/tasks/abc250_b
n, a, b = map(int, sys.stdin.readline().split())

t = ("." * b + "#" * b) * n
for i in range(n):
    for _ in range(a):
        if i % 2 == 0:
            print(t[:n * b])
        else:
            print(t[b:(n + 1) * b])
