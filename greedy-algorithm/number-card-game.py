import sys

# 数字カードゲーム
a, b = map(int, sys.stdin.readline().split())
c = []
for _ in range(a):
  temp = list(map(int, sys.stdin.readline().split()))
  temp.sort()
  c.append(temp[0])

c.sort()
print(c[-1])