import sys
from collections import deque

# 迷宮からの脱出
n, m = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # キューが空になるまでループ
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 範囲外のインデックスの場合
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # モンスターがいる場合
            if li[nx][ny] == 0:
                continue
            # 通路が見つかった場合
            if li[nx][ny] == 1:
                li[nx][ny] = li[x][y] + 1
                queue.append((nx, ny))

    return li[n - 1][m - 1]


print(bfs(0, 0))
