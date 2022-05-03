import sys

# 大数の法則
# 以下の方法だと、bが100億以上になった場合に制限時間をオーバーする可能性がある。
a, b, c = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))

d.sort()
# 最大値
first = d[-1]
# 2番目に大きい値
second = d[-2]

r = 0
while True:
  for _ in range(c):
    if b == 0:
      break
    r += first
    b -= 1
  if b == 0:
    break
  r += second
  b -= 1

print(r)