import sys

# 1になるまで
a, b = map(int, sys.stdin.readline().split())

cnt = 0

while a > 1:
  # aをbで割り切れる場合、割り算をする
  if a % b == 0:
    a //= b
  # 割り切れない場合は引き算をする
  else:
    a -= 1
  cnt += 1

print(cnt)
