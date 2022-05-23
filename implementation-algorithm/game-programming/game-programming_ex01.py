import sys

# ゲーム開発
n, m = map(int, sys.stdin.readline().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, sys.stdin.readline().split())
d[x][y] = 1

li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# キャラクターを左に回す
def turn_left():
    # グローバル変数を使用
    global direction
    direction -= 1
    if direction < 0:
        direction = 3


cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 前のマスに移動できる場合
    if d[nx][ny] == 0 and li[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    # 前のマスに移動できない場合
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 後ろのマスに移動できる場合
        if li[nx][ny] == 0:
            x = nx
            y = ny
        # 後ろのマスに移動できない場合
        else:
            break
        turn_time = 0

print(cnt)
