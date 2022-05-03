import sys

# 大数の法則
a, b, c = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))

d.sort()
# 最大値
first = d[-1]
# 2番目に大きい値
second = d[-2]

# 最大値が足される回数を計算
cnt = (b // (c + 1)) * c
cnt += b % (c + 1)

r = 0
r += cnt * first
r += (b - cnt) * second

print(r)