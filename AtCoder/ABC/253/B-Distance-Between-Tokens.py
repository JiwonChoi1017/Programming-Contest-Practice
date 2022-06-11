import sys

# B - Distance Between Tokens
# https://atcoder.jp/contests/abc253/tasks/abc253_b
h, w = map(int, sys.stdin.readline().split())
t = []
for i in range(h):
    temp = sys.stdin.readline().rstrip()
    idx = [i for i, x in enumerate(temp) if x == "o"]
    for j in idx:
        t.append((i, j))

result = abs(t[1][0] - t[0][0]) + abs(t[1][1] - t[0][1])
print(result)
