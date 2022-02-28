import sys

# 1になるまで
a, b = map(int, sys.stdin.readline().split())

cnt = 0

while True:
  target = (a // b) * b
  cnt += a - target
  a = target
  if a < b:
    break
  cnt += 1
  a //= b

cnt += a - 1
print(cnt)
