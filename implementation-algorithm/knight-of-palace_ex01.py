import sys

# 王室のナイト
a = sys.stdin.readline()
row = int(a[1])
column = int(ord(a[0])) - int(ord("a")) + 1

# 8つの方向を定義しておく
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

cnt = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        cnt += 1

print(cnt)
