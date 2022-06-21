import sys

# B - Enlarged Checker Board
# https://atcoder.jp/contests/abc250/tasks/abc250_b
n, a, b = map(int, sys.stdin.readline().split())

for i in range(n):
    for _ in range(a):
        if i % 2 == 0:
            s = ("." * b + "#" * b) * n
        else:
            s = ("#" * b + "." * b) * n
        print(s[0:len(s) // 2])
