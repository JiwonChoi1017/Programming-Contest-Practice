import sys

# 迷宮からの脱出
n, m = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(list(map(int, input())))

# 現在位置
li[0][0] = 2
cnt = 1

cur_n = 0
cur_m = 0


def find_exit(x, y):
    global cur_n
    global cur_m
    global cnt

    # 範囲外のインデックスの場合
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return

    # モンスターがいる場合
    if li[x][y] == 0:
        return

    # 出口を見つかった場合
    if li[n - 1][m - 1] == 2:
        return

    # 通路が見つかった場合
    if li[x][y] == 1:
        # 移動
        li[x][y] = 2
        cnt += 1
        cur_n = x
        cur_m = y
        return

    find_exit(x, y + 1)
    find_exit(x + 1, y)
    find_exit(x, y - 1)
    find_exit(x - 1, y)
    return


# 出口を見つかるまでループ
while li[n - 1][m - 1] != 2:
    find_exit(cur_n, cur_m)

print(cnt)
