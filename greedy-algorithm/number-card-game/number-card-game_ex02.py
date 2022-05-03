import sys

# 数字カードゲーム
a, b = map(int, sys.stdin.readline().split())
r = 0

for _ in range(a):
  temp = list(map(int, sys.stdin.readline().split()))
  # 数値の上限 + 1
  min_value = 10001
  # 現在の行から最小値を取得
  for i in temp:
    min_value = min(min_value, i)
  # rとmin_valueの中から最大値を抽出してrに格納
  r = max(r, min_value)

print(r)