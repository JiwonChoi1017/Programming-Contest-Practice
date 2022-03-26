import sys

# パーツ探し（分布数え上げソート）
n = int(sys.stdin.readline().rstrip())
# 1 < n < 1000000のため
n_list = [0] * 1000001

for i in map(int, sys.stdin.readline().split()):
    n_list[i] = 1

m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    print("yes" if n_list[i] > 0 else "no", end=" ")
