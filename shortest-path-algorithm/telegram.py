import heapq
import sys

# 電報
# ダイクストラ法
INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))


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


dijkstra(c)

filter_distance = list(filter(lambda i: 0 < i < INF, distance))
count = len(filter_distance)
dist = max(filter_distance) if count > 0 else 0

print(count, dist)
