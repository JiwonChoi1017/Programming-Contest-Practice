import sys

# B - Practical Computing
# https://atcoder.jp/contests/abc254/tasks/abc254_b
n = int(sys.stdin.readline().rstrip())
result = []

for i in range(0, n):
    temp = []
    for j in range(0, i + 1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(result[i - 1][j] + result[i - 1][j - 1])
    result.append(temp)

for i in result:
    print(*i)
