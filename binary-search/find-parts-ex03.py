import sys

# パーツ探し（set型（集合型）を使用）
n = int(sys.stdin.readline().rstrip())
n_list = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    print("yes" if i in n_list else "no", end=" ")
