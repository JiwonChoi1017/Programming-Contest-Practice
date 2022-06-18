import sys

# B - Batters
# https://atcoder.jp/contests/abc256/tasks/abc256_b
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
l = []

for i in a:
    l.insert(0, 0)
    l = [k + i for k in l]

p = len([i for i in l if i >= 4])
print(p)
