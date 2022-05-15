import sys

# ボウリングボール選び
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
bowling_ball_weight = [0] * 11

for x in li:
    # ボウリングボール数を格納
    bowling_ball_weight[x] += 1

result = 0

for i in range(1, m + 1):
    n -= bowling_ball_weight[i]
    # Aが選んだボール * Bが選べるボール数
    result += bowling_ball_weight[i] * n

print(result)
