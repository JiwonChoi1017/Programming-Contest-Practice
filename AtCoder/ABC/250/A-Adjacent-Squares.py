import sys

# A - Adjacent Squares
# https://atcoder.jp/contests/abc250/tasks/abc250_a
h, w = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())

result = 4

if r <= 1:
    result -= 1
if r >= h:
    result -= 1
if c <= 1:
    result -= 1
if c >= w:
    result -= 1

print(result)
