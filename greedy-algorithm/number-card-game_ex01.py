import sys

# 数字カードゲーム
a, b = map(int, sys.stdin.readline().split())
r = 0

for _ in range(a):
  temp = list(map(int, sys.stdin.readline().split()))
  # 現在の行から最小値を取得
  min_value = min(temp)
  # rとmin_valueの中から最大値を抽出してrに格納
  r = max(r, min_value)

print(r)