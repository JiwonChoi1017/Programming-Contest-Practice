import sys

# 大数の法則
a, b, c = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))
d.sort(reverse=True)

cnt = 0
r = 0
for _ in range(b):
  if cnt >= c:
    r += d[1]
    cnt = 0
    continue

  cnt += 1
  r += d[0]

print(r)