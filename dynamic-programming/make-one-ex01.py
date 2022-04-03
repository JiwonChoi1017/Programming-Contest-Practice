import sys

# 1にする
x = int(sys.stdin.readline().rstrip())
# xの上限が30000のため
d = [0] * 30001

# 下記の動画を参考
# https://www.youtube.com/watch?v=5Lu34WIx2Us&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
