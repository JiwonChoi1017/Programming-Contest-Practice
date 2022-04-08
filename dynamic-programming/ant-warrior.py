import sys

# 蟻戦士
n = int(sys.stdin.readline().rstrip())
k = list(map(int, sys.stdin.readline().split()))
d = [0] * 101
d[0] = k[0]
d[1] = k[1]

for i in range(2, n):
    d[i] = max(d[0:i - 1]) + k[i]

m = max(d)
print(m)
