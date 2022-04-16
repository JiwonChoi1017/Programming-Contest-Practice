import heapq
import sys

# 未来都市
# ダイクストラ法
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

x, k = map(int, sys.stdin.readline().split())

start = [1, k]
end = [k, x]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


re = 0
for i, v in enumerate(start):
    dijkstra(v)
    if distance[end[i]] == INF:
        re = -1
        break
    else:
        re += distance[end[i]]

print(re)
